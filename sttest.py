#!/usr/bin/python

from Tkinter import *
from ScrolledText import *
import thread, subprocess, sys, os, fcntl, time, Queue, select, re, copy
import stbehaviour	# FUCK YOU IT WILL ALWAYS BE BEHAVIOUR NOT BEHAVIOR


class skulltagBotWindow(Frame):
	def __init__(self, args='', parent=None):
		Frame.__init__(self, parent)
		
		self.args = args
		self.flags = [0,0,0,0,0]
		self.history = []
		self.players = {'amount': 0}
		self.historyMarker = 0
		self.playerinfoRE = re.compile("([0-9]+)\. ([^%]+?) - IP \(([0-9\.]+:[0-9]+)\)")
		
		for flag, index in (('+dmflags', 0), ('+dmflags2', 1), ('+dmflags3', 2), ('+compatflags', 3), ('+compatflags2', 4)):
			if flag in self.args:
				try:
					self.flags[index] = int(self.args[self.args.index(flag)+1])
				except:
					pass
		
		self.outputText = ScrolledText()
		self.outputText.config(state=DISABLED)
		self.outputText.pack(expand=1, fill='both', anchor='n')
		self.inputTextText = StringVar()
		self.inputText = Entry(textvariable=self.inputTextText)
		self.inputText.bind('<Return>', self.writeLine)
		self.inputText.bind('<Up>', self.upOneHist)
		self.inputText.bind('<Down>', self.downOneHist)
		self.inputText.pack(fill='x', anchor='s')
		self.outputText.tk.call('tk', 'scaling', 1)
		
		self.outputQueue = Queue.Queue()		# just to be orderly
		self.inputQueue = Queue.Queue()			# same
		self.inQLock = thread.allocate_lock()	# well durrrrrr
		self.outQLock = thread.allocate_lock()
		
		thread.start_new(self.startSkulltag, (None,))
		
		self.pack()
	
	def startSkulltag(self, deadArg):
		self.skulltag = subprocess.Popen(['/usr/games/skulltag/skulltag-server', '+sv_markchatlines 1']+self.args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
		self.stdinPoll = select.poll()
		self.stdinPoll.register(self.skulltag.stdout, select.POLLIN)
		self.stdoutPoll = select.poll()
		self.stdoutPoll.register(self.skulltag.stdout, select.POLLOUT)
		thread.start_new(self.rwLoop, (None,))
	
	def rwLoop(self, deadArg):
		self.readLine()
		try:										#check for input
			output = self.inputQueue.get(block=0)
		except Queue.Empty:
			pass
		else:
			self.inQLock.acquire()
			self.outputText.config(state=NORMAL)
			self.outputText.insert(END, output)		#put it in the main window
			self.outputText.scan_mark(100000, 1)
			self.outputText.scan_dragto(10, 1)
			try:
				lscbot = stbehaviour.LSCParserBot(output, copy.deepcopy(self.players), *self.flags[:])
				chatText = lscbot.get()
						
				if chatText[0]:
					self.skulltag.stdin.flush()
					self.skulltag.stdin.write("say " + chatText[0] + '\n')
				
				self.flags = chatText[2:]
			except:
				import traceback
				print "%s\n%s" % (sys.exc_info()[0], sys.exc_info()[1])
				print traceback.print_tb(sys.exc_info()[2])
				self.cquit()
			self.outputText.config(state=DISABLED)
			self.inQLock.release()
		
		try:										#now for output
			output = self.outputQueue.get(block=0)
		except Queue.Empty:
			pass
		else:
			self.outQLock.acquire()
			self.skulltag.stdin.write(output)
			self.skulltag.stdin.flush()
			self.outQLock.release()
		self.after(5, self.rwLoop, (None,))
	
	def readLine(self):
		output = ''
		scrollAmount = 0
		if self.skulltag.poll():
			output = '\n\n - Terminated - '
			sys.exit()
		else:
			pollin = self.stdinPoll.poll(1)
			while pollin:
				pollin = pollin[0]
				if pollin[1] == 1:
					self.skulltag.stdout.flush()
					output += self.skulltag.stdout.readline()
					scrollAmount += 1
				pollin = self.stdinPoll.poll(1)
		
		if output == 'NETWORK_LaunchPacket: Permission denied\n' or output == 'NETWORK_LaunchPacket: Address 192.168.1.255:15101\n':
			output = ''
		
		if output:
			self.outputText.yview_scroll(16*((len(output)/80)+1)+(scrollAmount*16), 'pixels')
			
		self.inputQueue.put(output)
	
	def upOneHist(self, deadArg):
		if self.historyMarker <= -len(self.history):
			return
		
		self.historyMarker -= 1
		self.inputText.delete(0, END)
		self.inputText.insert(END, self.history[self.historyMarker])
		
	def downOneHist(self, deadArg):
		if self.historyMarker >= -1:
			self.inputText.delete(0, END)
			self.historyMarker = 0
			return
		
		self.historyMarker += 1
		self.inputText.delete(0, END)
		self.inputText.insert(END, self.history[self.historyMarker])
		
	def writeLine(self, deadArg):
		self.inputText.insert(END, ' ')
		output = self.inputTextText.get()
		self.history += [output[:-1]]
		self.historyMarker = 0
		if output[0] == ':':
			output = 'say ' + output[1:]
		if output.strip() == 'reset_lscbot':
			self.inputText.delete(0, END)
			self.skulltag.stdin.write("say Resetting the LSC Bot - should be a second\n")
			self.skulltag.stdin.flush()
			reload(stbehaviour)
			self.skulltag.stdin.write("say or less\n")
			self.skulltag.stdin.flush()
		else:
			self.inputText.delete(0, END)
			self.outputQueue.put(output)
				
		
	def cquit(self):
		for i in range(32):
			self.skulltag.stdin.write("kick_idx %s \" -- Server quit by host -- \"\n" % (i + 1))
			self.skulltag.stdin.flush()
		self.skulltag.stdin.write("error_fatal \"-- Server quit by host --\"")
		time.sleep(1)
		self.skulltag.terminate()
		self.quit()

if __name__ == "__main__":
	root = Tk()
	mainwin = skulltagBotWindow(sys.argv[1:])
	root.protocol("WM_DELETE_WINDOW", mainwin.cquit)
	root.title("Test")
	mainwin.mainloop()
	sys.exit()
	
