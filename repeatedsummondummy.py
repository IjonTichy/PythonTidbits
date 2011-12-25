import time

def repeatedSummon(actor, summonCount, delay=0):
	if summonCount > 0:
		summon(actor)
		time.sleep(float(delay)/35)
		repeatedSummon(actor, summonCount-1, delay)
