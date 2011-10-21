#!/usr/bin/python
import os, re
dateExtract = re.compile("\[(\d*)-(\d*)-(\d*)\D*(\d*)-(\d*)-(\d*)\]")
dateGet = re.compile("\D*(\d*)-(\d*)-(\d*)\D*(\d*):(\d*):(\d*)")

def cleanup(dirToClean, beforeDate):
	"A function that cleans up DoomRL's mortem and screenshot folder. :)"
	os.chdir(dirToClean)

	#get directory list
	for file in os.popen("dir").readlines():
		noDelete = 0
		#get file; ignore '!readme.txt'
		if file[0] != '!':
			file = file.rstrip()
			TestDate = re.match(dateExtract, file).groups() #get day file was taken

			#this is to decide whether to delete file or not
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
