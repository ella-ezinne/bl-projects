import platform
import psutil
import socket
import os
from datetime import datetime, timedelta

def get_system_info():
    print("=== System Information ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def get_cpu_info():
    print("\n===CPU Info ===")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU usage per core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_memory_info():
    print("\n=== Memory Info ===")
    mem = psutil.virtual_memory()
    print(f"Total: {get_size(mem.total)}")
    print(f"Available: {get_size(mem.available)}")
    print(f"Used: {get_size(mem.used)} ({mem.percent}%)")

def get_disk_info():
    print("\n=== Disk Info ===")
    for partition in psutil.disk_partitions():
        print(f"Device: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Total Size: {get_size(usage.total)}")
        print(f"  Used: {get_size(usage.used)}")
        print(f"  Free: {get_size(usage.free)}")
        print(f"  Percentage: {usage.percent}%")

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