#!/usr/bin/python3.0
import os, re

def doomrlCleanup(dirToClean):
    "A function that cleans up DoomRL's mortem and screenshot folder. :)"
    os.chdir(dirToClean)

    #get directory list
    for file in os.popen("dir").readlines():
        noDelete = 0
        #get file; ignore '!readme.txt'
        if file[0] != '!':
            file = file.rstrip()
            TestDate = re.match(dateExtract, file).groups() #get day file was taken

            #this is to decide whether to delete file or not
            for i in range(6):
                if int(cleanupDate[i]) > int(TestDate[i]):
                    break
            else:
                noDelete = 1 

            # POSIX systems on if; windows on elif
            if noDelete == 0 and os.name == 'posix':
                os.system("rm %s" % file)
            elif noDelete == 0 and os.name[:3] == 'win': 
                os.system("del %s" % file)               
    
    os.chdir('..')


if __name__ == '__main__':
    date = None
    Dir = None
    startSucceeded = False
    mortemScreen = 0
    dateExtract = re.compile("\[(\d*)-(\d*)-(\d*)\D*(\d*)-(\d*)-(\d*)\]")
    dateGet = re.compile("\D*(\d*)-(\d*)-(\d*)\D*(\d*):(\d*):(\d*)")
    print("""
%s
DoomRL mortem/screenshot cleanup tool
By Generic_Guy (also Generic)
Looks through your screenshot and mortem folder (or
just one, if you please), and removes any screenshots
and mortems that were made before the date you specified
%s""" % ("-" * 25, "-" * 25))
    while not startSucceeded:
        startSucceeded = True
        while mortemScreen not in ("0", "1", "2"):
            mortemScreen = input("\nMortem (0), screenshot (1), or both (2): ")
        if os.name == "posix":
            print("Current dir: " + os.popen("pwd").read().rstrip())
        elif os.name[:3] == "win":
            print("Current dir: " + os.popen("cd").read().rstrip())
        while not Dir:
            Dir = input("DoomRL directory: ")
        while not date:
            date = input("Cleanup date (in day-month-year hour:minute:second): ")
        try:
            cleanupDate = re.match(dateGet, date).groups()
        except AttributeError:
            print("Invalid date; try again")
            startSucceeded = False
            date = None
        try: os.chdir(Dir)
        except:
            if date == None:
                print("Also, invalid dir")
            else:
                print("Invalid dir; try again")
                startSucceeded = False
            Dir = None
    if mortemScreen in ("0", "2"):
        print("Cleaning up mortems")
        doomrlCleanup('mortem')
    if mortemScreen in ("1", "2"):
        print("Cleaning screenshots")
        doomrlCleanup('screenshot')
        print("Cleanup done")
    if os.name[:3] == "win":
        input("\nPress Enter")
