#!/usr/bin/python

import sys

newList = []

for i in range(18):
	tempList = []
	for j in range(3):
		tempStr = 'bacon'
		while tempStr == 'bacon':
			try:
				tempStr = raw_input("p. %s - n. %s: " % (i+1, j+1))
				tempStr = eval(tempStr)
				if int(tempStr) != float(tempStr):
					tempStr = float(tempStr)
				else:
					tempStr = int(tempStr)
			except ValueError:
				print "\ninvalid number\n"
				tempStr = 'bacon'
			except ValueError:
				print "\ninvalid number\n"
				tempStr = 'bacon'
			except SyntaxError:
				print "\nenter something\n"
				tempStr = 'bacon'
		tempList += [tempStr]
	newList += [tempList]


print >> sys.stderr, newList
