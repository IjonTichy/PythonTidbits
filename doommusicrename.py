for file in sorted(directory):
    print(file)
    newname = file.split('.')[0]
    names = newname.split('-')
    newnames = []
    #print('\t', names, sep='')
    
    for name in names:
        name = name.upper()
        if name[:3] == 'MAP':
            name2 = 'MAP{0:0>2}.mp3'.format(name[3:])
        else:
            try:
                junk = int(name)
            except:
                name2 =  name+'.mp3'
            else:
                name2 = 'MAP{0:0>2}.mp3'.format(name)
        
        newnames.append(name2)
        #print('\t\t{0}'.format(name2))
    
    movename = newnames.pop()
    for name in newnames:
        shutil.copy(file, name)
    
    shutil.move(file, movename)
