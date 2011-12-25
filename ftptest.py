#!/usr/bin/python

from getpass import getpass
import ftplib, socket, sys
actionslist = ('put', 'get', 'rm', 'cd', 'ls')


success = 0
while not success:
	try:
		site = None
		while not site:
			site = raw_input('connect to: ').strip()
		ftp = ftplib.FTP(site)
	except socket.gaierror:
		print 'server doesn\'t exist - try again'
	else:
		success = 1

success = 0
while not success:
	try:
		user = raw_input('user: ')
		pswd = getpass('pswd: ')
		ftp.login(user, pswd)
	except ftplib.error_perm:
		print 'user/password incorrect'
	else:
		success = 1


action = ''
while 1:
	success = 0
	while action.lower() not in actionslist:
		action = raw_input('put file, get file, cd, quit? ').strip()
	
	if action.lower() == 'quit': break
	
	if action.lower() == 'get':
		ftp.dir()
		while not success:
			try:
				file = raw_input('get which file? ').strip()
				ftp.retrbinary('RETR %s' % file, sys.stdout.write)
			except ftplib.error_perm:
				print 'file doesn\'t exist - try again'
			else:
				print
				success = 1
	
	if action.lower() == 'ls':
		ftp.dir()
	
	
	
	if action.lower() == 'put':
		import os
		counter = 0
		for i in os.listdir('.'):
			if i[0] != '.':
				if counter == 1:
					print '%-40s' % i
				else:
					print '%-40s' % i,
				counter = not counter
		if counter: print
		
		while not success:
			try:
				file = raw_input('open which file?').strip()
				localfile = open(file, 'rb')
				ftp.storbinary('STOR %s' % file, localfile)
			except IOError:
				print 'file doesn\'t exist - try again'
			except ftplib.error_perm:
				print 'you do not have proper permissions'
				break
			else:
				success = 1
	action = ''
				
ftp.close()
print 'success'
