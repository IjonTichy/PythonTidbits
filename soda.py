#!/usr/bin/python
def snowball():
	numS = None
	while not numS:
		try: numS = int(raw_input("Amount of students attending: "))
		except ValueError: print "NaN"
	soda24, numS = divmod(numS, 24)
	soda6, numS = divmod(numS, 6)
	soda1, numS = numS, 0
	print "You'll need:\n%s 24-pack%s of soda\n%s 6-pack%s of soda\n%s single soda%s" % \
	(soda24, "" if soda24 == 1 else "s", soda6, "" if soda6 == 1 else "s", soda1, "" if soda1 == 1 else "s")

if __name__ == "__main__": snowball()
	
