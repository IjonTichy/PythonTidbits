#!/usr/bin/python
import time, os
from Tkinter import *

def startClean():
	if mClearV.get() == 1:
		cleanup('%s/mortem'%dirEntry.get(), '[%s %s]'%(dateEntry.get(),timeEntry.get()))
	if sClearV.get() == 1:
		cleanup('%s/screenshot'%dirEntry.get(), '[%s %s]'%(dateEntry.get(),timeEntry.get()))

def cleanup(dirToClean, beforeDate):
	"A function that cleans up DoomRL's mortem and screenshot folder. Now get me some beer, I'm lazy. ;P"
	os.chdir(dirToClean)

	# get directory list
	for file in os.popen("dir").readlines():
		noDelete = 0
		# get file; ignore '!readme.txt'
		if file[0] != '!':
			file = file.rstrip()
			TestDate = re.match(dateExtract, file).groups() #get day file was taken

			# this is to decide whether to delete file or not
			for i in range(6):
				if int(beforeDate[i]) > int(TestDate[i]):
					break
			else:
				noDelete = 1 

			# POSIX systems on if; windows on elif
			if noDelete == 0 and os.name == 'posix':
				os.system("rm %s" % file)
			elif noDelete == 0 and os.name[:3] == 'win': 
				os.system("del %s" % file)			   
	
	os.chdir('..')




#get date, time
cT = time.localtime()
curDate = '%s-%s-%s'%(cT[2],cT[1],cT[0])
curTime = '%.2d:%.2d:%.2d'%(cT[3],cT[4],cT[5])
del cT

# initialize everything
root = Tk()
dateEntry = Entry(root,width=15);dateEntry.insert(0,curDate)	# these weren't exactly necessary,
timeEntry = Entry(root,width=15);timeEntry.insert(0,curTime)	# but I decided to be nice, and
dirEntry = Entry(root,width=40);dirEntry.insert(0,os.getcwd())	# save you some typing (just some) :)
sClearV = IntVar()
sClearB = Checkbutton(root,text="Screenshots",variable=sClearV)
mClearV = IntVar()
mClearB = Checkbutton(root,text="Mortems",variable=mClearV)

# grid everything, make static objects
Label(text="Date:").grid(row=0,column=0,sticky='W')
dateEntry.grid(row=0,column=1,sticky='EW')
Label(text="Time:").grid(row=0,column=2,sticky='E')
timeEntry.grid(row=0,column=3,sticky='W')
Label(text="Dir:").grid(row=1,column=0,sticky='W')
dirEntry.grid(row=1,column=1,columnspan=3,sticky='EW')
Label(text='Clean up:').grid(row=2,column=0)
mClearB.grid(row=2,column=1)
sClearB.grid(row=2,column=2)
Button(text="Clean up",command=startClean).grid(row=2,column=3)
# kick it all off :D
root.title('DoomRL Cleanup')
root.mainloop()
