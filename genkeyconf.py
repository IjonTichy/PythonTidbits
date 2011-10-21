baseStr = "addslotdefault {0} \"Uber-{1}\""

for n, w in ((1, "Chainsaw"), (1, "Fist"), (2, "Pistol"), (3, "Shotgun"),
             (3, "Super Shotgun"), (4, "Chaingun"), (4, "Minigun"),
             (5, "Rocket Launcher"), (5, "Grenade Launcher"), (6, "Plasma Rifle"),
             (6, "Railgun"), (7, "BFG9000"), (7, "BFG10k")):
	print(baseStr.format(n, w))
