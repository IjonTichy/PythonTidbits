from math import floor

baseStr="""			HudMessage(s:"A"; HUDMSG_PLAIN, 861, CR_GREEN, 0.48, 0.146, 30.0);
			HudMessage(s:"Stats for ", n:pln+1; HUDMSG_PLAIN, 859, CR_WHITE, 0.5, 0.13, 30.0);
			HudMessage(s:"Max HP"; HUDMSG_PLAIN, 842, CR_GREEN, 0.43, 0.15, 30.0);
			HudMessage(s:"Damage+"; HUDMSG_PLAIN, 843, CR_GREEN, 0.43, 0.17, 30.0);
			HudMessage(s:"Regen Time"; HUDMSG_PLAIN, 844, CR_GREEN, 0.43, 0.19, 30.0);
			HudMessage(s:"Resupply Time"; HUDMSG_PLAIN, 845, CR_GREEN, 0.43, 0.21, 30.0);
			HudMessage(s:"Speed"; HUDMSG_PLAIN, 846, CR_GREEN, 0.43, 0.23, 30.0);
			HudMessage(s:"Jump Z"; HUDMSG_PLAIN, 847, CR_GREEN, 0.43, 0.25, 30.0);
			HudMessage(i:health[(pln*3)]; HUDMSG_PLAIN, 852, CR_YELLOW, 0.57, 0.15, 30.0);
			HudMessage(i:damage[(pln*3)]; HUDMSG_PLAIN, 853, CR_YELLOW, 0.57, 0.17, 30.0);
			HudMessage(f:(regen[(pln*3)]<<16)/35; HUDMSG_PLAIN, 854, CR_YELLOW, 0.57, 0.19, 30.0);
			HudMessage(f:(resupply[(pln*3)]<<16)/35; HUDMSG_PLAIN, 855, CR_YELLOW, 0.57, 0.21, 30.0);
			HudMessage(f:speed[(pln*3)]; HUDMSG_PLAIN, 856, CR_YELLOW, 0.57, 0.23, 30.0);
			HudMessage(f:jump[(pln*3)]; HUDMSG_PLAIN, 857, CR_YELLOW, 0.57, 0.25, 30.0);"""

baseList = baseStr.split('\n')
baseList2 = []
baseList3 = []

def onlyNums(string):
	ret = ''
	for i in string:
		if i in '0123456789.':
			ret += i
	ret = float(ret)
	if ret != int(ret):
		return float(ret)
	else:
		return int(ret)


for i in baseList:
	j = i.split(';')[:2]
	m = j[1].split(',')
	j = [j[0]] + m
	
	for (l, k) in enumerate(j):
		j[l] = k.strip()
	baseList2 += [j]
	
for (j, i) in enumerate(baseList2):
	n = []
	i[:0] = ['HudMessage(']
	i[1] = i[1][len('HudMessage('):]
	for (l, k) in enumerate(i[2:]):
		for m in k:
			if m in '0123456789.':
				k = onlyNums(k)
				break
		n += [k]
	
	baseList3 += [i[:2] + n]

for i in baseList3:
	i[5] = float(floor(i[5]*800))
	i[6] = float(floor(i[6]*600))
	tempStr = '%s%s; %s, %s, %s, %s, %s, %s);' % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
	print(tempStr)


