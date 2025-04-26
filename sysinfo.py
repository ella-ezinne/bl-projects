import platform
import psutil
import socket
import json
import os
from datetime import datetime, timedelta

def get_system_info():
    return{
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    

def get_cpu_info():
    return{
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "CPU usage per core": [f"Core {i}: {percentage}%" for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))],

        "Total CPU Usage": f"{psutil.cpu_percent()}%"
    }


def get_memory_info():
    mem = psutil.virtual_memory()
    return{
        "Total Memory": get_size(mem.total),
        "Available Memory": get_size(mem.available),
        "Used Memory": get_size(mem.used),
        "Memory Usage Percentage": f"{mem.percent}%"
    }

def get_disk_info():
    disks = {}
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disks[partition.device] = {
            "Mountpoint": partition.mountpoint,
            "File System Type": partition.fstype,
            "Total Size": get_size(usage.total),
            "Used": get_size(usage.used),
            "Free": get_size(usage.free),
            "Percentage": f"{usage.percent}%"
        }
    return disks

def get_network_info():
    print("\n=== Network Info ===")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

def get_up_time():
    print("\n=== System Uptime ===")
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    print(f"Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Uptime: {str(uptime).split('.')[0]}")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f} {unit}{suffix}"
        bytes /= factor

if __name__== "__main__":
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_network_info()
    get_up_time()