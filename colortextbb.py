#!/usr/bin/python3.1

baseStr = input('string: ')
baseLen = len(baseStr)
turnonloop = 0
red = 255
green = 0
blue = 0
COLORMOD = 6

print()

for i in baseStr:
	loop = ''
	
	if red == 255 and blue != 0:
		loop = 'b2'
		blue -= ((255.0 / baseLen) * COLORMOD)
		blue = int(blue)
		if blue < 0:
			green += -blue
			blue = 0
	
	elif red == 255 and green != 255:
		loop = 'r1'
		green += ((255.0 / baseLen) * COLORMOD)
		green = int(green)
		if green > 255:
			red -= green - 255
			green = 255
	
	elif green == 255 and red != 0:
		loop = 'r2'
		red -= ((255.0 / baseLen) * COLORMOD)
		red = int(red)
		if red < 0:
			blue += -red
			red = 0
	
	elif green == 255 and blue != 255:
		loop = 'g1'
		blue += ((255.0 / baseLen) * COLORMOD)
		blue = int(blue)
		if blue > 255:
			blue -= blue - 255
			blue = 255
	
	elif blue == 255 and green != 0:
		loop = 'g2'
		green -= ((255.0 / baseLen) * COLORMOD)
		green = int(green)
		if green < 0:
			red += -green
			green = 0
	
	elif blue == 255 and red != 255:
		loop = 'b1'
		red += ((255.0 / baseLen) * COLORMOD)
		red = int(red)
		if red > 255:
			blue -= red - 255
			red = 255
	
	hexRed, hexBlue, hexGreen, = hex(red)[2:], hex(green)[2:], hex(blue)[2:]
	hexRed = '0'*(2-len(hexRed))+hexRed
	hexGreen = '0'*(2-len(hexGreen))+hexGreen
	hexBlue = '0'*(2-len(hexBlue))+hexBlue
	if turnonloop:
		colorStr = "%s: [color=#%s%s%s]%s[/color] (%s, %s, %s)\n" % (loop, hexRed, hexBlue, hexGreen, i, red, green, blue)
	else:
		colorStr = "[color=#%s%s%s]%s[/color]" % (hexRed, hexBlue, hexGreen, i)
	print(colorStr, end='')

print()
