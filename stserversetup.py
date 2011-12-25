dmflagsList = ('No health spawn', 'No powerup spawn', 'Weapons stay', 'Fall Damage (ZDoom)', 'Fall Damage (Hexen)', ' ', 'Same map', 'Spawn farthest', 'Force respawn', 'No armor spawn', 'No exit', 'Infinite ammo', 'No monsters', 'Respawning monsters', 'Respawning items', 'Fast monsters', 'No jump', 'No freelook', 'Respawning mega-powerups', '90 FOV only', 'Only campaign weapons', 'No crouch', 'Lose inventory on death', 'Lose keys on death', 'Keep weapons on death', 'Lose armor on death', 'Lose powerups on death', 'Lose ammo on death', 'Lose half ammo on death')

dmflags2List = (' ', 'Drop weapon on death', 'No (normal) runes', 'Instant flag/skull return', 'No team switching', 'Server chooses teams', 'Double ammo', 'Degenerate HP over max', 'BFG aiming', 'Respawning barrels', 'No respawn invuln.', 'Shotgun start', 'Spawn where died', 'Keep team on map change', ' ', ' ', ' ', ' ', 'Forced OpenGL defaults', ' ', 'Point on 100 damage', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'No multiplayer actors')

dmflags3List = (' ')*30

compatflagsList = ('Find shortest texture', 'Buggy stairbuilding', 'Pain Elemental 20 Lost Soul limit', 'Local pickups', 'Infinitely tall actors', 'Silent BFG trick', 'Wallrunning', 'Items dropping on floor', 'Special lines blocking use', 'No door light effect', 'Raven speed scrollers', 'Sector-based sound targeting', 'Max Health bonus limit', ' ', 'No monster movement dropoff', 'Additive scrolling sectors', 'Blursphere not stopping detection', 'Literal air friction', 'Grabbing items through walls', 'Allow instant respawn', 'Tauntless', 'Doom sound curve', 'Old intermission screen', 'Pointless stealth monsters', 'Infinite height explosions', 'No crosshair', 'Forced weapon switch on pickup')

compatflags2List = ('Clientside net scripts', 'Full button info sending', 'No \'land\' command')

dmflagsFlags = ()
dmflags2Flags = ()
dmflags3Flags = ()
compatflagsFlags = ()
compatflags2Flags = ()

for i in range(len(dmflagsList)):
	dmflagsFlags += ((dmflagsList[i], 2**i),)

print 'dmflagsList = %s\n' % (dmflagsFlags,)
