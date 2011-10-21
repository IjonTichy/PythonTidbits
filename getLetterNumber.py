#!/usr/bin/python3.1

def getNumberLetter(let1, num1, let2, num2, samples=1):
    
    if samples <= 0:
    	return
    
    let1Val = ord(let1.upper())-ord('A')
    let2Val = ord(let2.upper())-ord('A')
    frame1 = let1Val+(num1 * 26)
    frame2 = let2Val+(num2 * 26)
    frameaverage = (frame1+frame2) // 2
    ret = divmod(frameaverage, 26)
    ret = (chr(ret[1]+ord('A')), ret[0])
    samples -= 1
    
    if samples > 0:
        result1 = getNumberLetter(let1, num1, ret[0], ret[1], samples)
        result2 = ret
        result3 = getNumberLetter(ret[0], ret[1], let2, num2, samples)
        
        
        ret = ()
        
        if len(result1) > 2:
            ret1 = ()
            for i in result1:
            	ret1 += (i,)
        else:
            ret1 = (result1,)
        
        ret2 = result2
        
        if len(result3) > 2:
            ret3 = ()
            for i in result3:
            	ret3 += (i,)
        else:
            ret3 =  (result3,)
        
        ret = ret1+(ret2,)+ret3
    
    return ret

if __name__ == "__main__":
	argList = [["letter 1", ""], ["number 1", 0], ["letter 2", ""], ["number 2", 0], ["sample count", 2]]
	for (argN, arg) in enumerate(argList):
		success = 0
		newArg = None
		while not success:
			success = 1
			newArg = input("%s? - " % arg[0])
			if type(arg[1]) == type(''):
				from string import ascii_letters
				if len(newArg) != 1:
					success = 0
					print("letter must be one character")
				elif newArg not in ascii_letters:
					success = 0
					print("letter must be an ascii letter")
			
			
			if type(arg[1]) == type(0):
				try:
					newArg = int(newArg)
				except:
					success = 0
					print("number must be an integer")
				else:
					if newArg < 1:
						success = 0
						print("number must be higher than 0")
		
		argList[argN][1] = newArg
	
	argList2 = [arg[1] for arg in argList]
	
	print(((argList2[0], argList2[1]),) + getNumberLetter(*argList2) + ((argList2[2], argList2[3]),))
