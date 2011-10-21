baseStr = """
actor {0}: Weapon
{{
  States
  {{
  Select:
    TNT1 A 0 A_GiveInventory("{1}")
    TNT1 A 0 A_TakeInventory("{0}")
    TNT1 A 0 A_SelectWeapon("{1}")
    TNT1 A 1 A_Raise
    loop
  
  Deselect:
    TNT1 A 1 A_Lower
    loop
  
  Ready:
    TNT1 A 0 A_GiveInventory("{1}")
    TNT1 A 1 A_WeaponReady
    loop
  
  Fire:
    TNT1 A 1 A_GiveInventory("{1}")
    goto Ready
  }}
}}
"""

for n, w in ((1, "Chainsaw"), (1, "Fist"), (2, "Pistol"), (3, "Shotgun"),
             (3, "Super Shotgun"), (4, "Chaingun"), (4, "Minigun"),
             (5, "Rocket Launcher"), (1, "Grenade Launcher"), (6, "Plasma Rifle"),
             (6, "Railgun"), (7, "BFG9000"), (7, "BFG10k")):
    
    w1 = w.replace(" ", "")
    w2 = "Uber-{0}".format(w)
    
    print(baseStr.format(w1, w2))
