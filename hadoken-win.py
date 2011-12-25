#!/usr/bin/python

import string, sys

REPITIONS = 5

ALIASTYPES = {"zdoom": "Name=%s\nCommand=%s", "quake 2": "alias %s \"%s\""}
iniType = "quake 2"

def pollUntilAnswer(initString):
	ret = None
	while not ret: ret = raw_input(initString)
	return ret
def batchReplace(line, *replaces):
	newLine = ""
	for char in line:
		for replacement in replaces:
			if char != char.replace(*replacement):
				newChar = char.replace(*replacement)
				break
		else:
			newChar = char
		newLine += newChar
	
	return newLine


def formatAlias(name, command): # change me if necessary
	return ALIASTYPES[iniType] % (name, command)



if len(sys.argv) > 1:
	if sys.argv[1].lower() in ['st', 'zdoom', 'gzdoom', 'skulltag']:
		iniType = "zdoom"
		

print """
Exponential Alias Generator - generates aliases that run multiple aliases that run multiple aliases...
Current alias call count is %i, and current alias type is %s
""" % (REPITIONS, iniType)

name = ""
try:
	while not name:
		name = pollUntilAnswer("name?  ")
		if name[0] not in string.ascii_letters:
			name = ""
			print "invalid name"
		for char in name:
			if char not in (string.ascii_letters + string.digits + '_'):
				name = ""
				print "invalid name"
				break

	nameFirst = name[0]
	
	action = name
	while action == name:
		action = pollUntilAnswer("action?  ")
		newAction = batchReplace(action, ('"', '\\"'), ('\\', '\\\\')) # we might need action later
		if name == action:
			print "invalid action - infinite loop imminent"

	count = "a" # this will never become an integer
	while count == "a":
		count = pollUntilAnswer("count?  ")
		try:
			count = int(count)
		except ValueError:
			print "invalid count"
			count = "a"
except KeyboardInterrupt:
	print "\nexiting"
	sys.exit()

print "\n"*1, # make output explicit

printList = [formatAlias(name, action)]


for (num, oldNum) in zip(range(1, count+1), range(count)):
	repName = "%s%s" % (nameFirst, num)		# name = pie, repName = p1, etc.
	if repName == name:
		print "\n   --- ABORTING --- \nINFINITE LOOP IMMINENT"
		break
	if oldNum == 0:		# first iteration?
		oldRepName = name
	else:
		oldRepName = "%s%s" % (nameFirst, oldNum)
	
	repCommand = ';'.join([oldRepName]*REPITIONS)
	printList += [formatAlias(repName, repCommand)]
else:
	for i in printList: print i


