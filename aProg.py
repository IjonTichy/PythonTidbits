#!/usr/bin/python3

import sys
from decimal import *

baseStr = \
"""			HudMessage(s:"A"; HUDMSG_PLAIN, 861, CR_GREEN, 0.12, 0.09, 2.0);
			HudMessage(s:"Max HP"; HUDMSG_PLAIN, 842, CR_GREEN, 0.16, 0.1, 2.0);
			HudMessage(s:"Damage+"; HUDMSG_PLAIN, 843, CR_GREEN, 0.16, 0.12, 2.0);
			HudMessage(s:"Regen Time"; HUDMSG_PLAIN, 844, CR_GREEN, 0.16, 0.14, 2.0);
			HudMessage(s:"Resupply Time"; HUDMSG_PLAIN, 845, CR_GREEN, 0.16, 0.16, 2.0);
			HudMessage(s:"Speed"; HUDMSG_PLAIN, 846, CR_GREEN, 0.16, 0.18, 2.0);
			HudMessage(s:"Jump Z"; HUDMSG_PLAIN, 847, CR_GREEN, 0.16, 0.2, 2.0);
			HudMessage(i:health[(pln*3)]; HUDMSG_PLAIN, 852, CR_YELLOW, 0.3, 0.1, 2.0);
			HudMessage(i:CheckInventory("LevelDamageCounter"); HUDMSG_PLAIN, 853, CR_YELLOW, 0.3, 0.12, 2.0);
			HudMessage(f:(regen[(pln*3)]<<16)/35; HUDMSG_PLAIN, 854, CR_YELLOW, 0.3, 0.14, 2.0);
			HudMessage(f:(resupply[(pln*3)]<<16)/35; HUDMSG_PLAIN, 855, CR_YELLOW, 0.3, 0.16, 2.0);
			HudMessage(f:speed[(pln*3)]; HUDMSG_PLAIN, 856, CR_YELLOW, 0.3, 0.18, 2.0);
			HudMessage(f:jump[(pln*3)]; HUDMSG_PLAIN, 857, CR_YELLOW, 0.3, 0.2, 2.0);"""

baseStr2 = "HudMessage(%s; %s, %s, %s, %s, %s, %s);"

bsList = []
bsList2 = []
bsList3 = []
bsList4 = []
bsList5 = []

for i in baseStr.split('\n'):
	bsList += [i[14:-2]]

for i in bsList:
	bsList2 += [i.split(';')]

for i in bsList2:
	bsList3 = i[1].split(',')
	bsList4 = []
	for j in bsList3:
		try:
			j = Decimal(j)
			if int(j) == j:
				bsList4 += [int(j)]
			else:
				bsList4 += [Decimal(j)]
		except:
			bsList4 += [j.strip()]
	bsList5 += [[i[0].strip()] + bsList4]

for i in bsList5:
	i[4] = i[4] + (Decimal('0.5')-((Decimal('0.3') + Decimal('0.16')) / 2))
	i[5] = Decimal('0.7')+i[5]
	 
for i in bsList5:
	print(baseStr2 % tuple(i))
