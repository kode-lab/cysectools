# Kode Blue, 10/29/2020
# Script for finding Hardware Informaiton about a machine

import platform
import psutil
from datetime import datetime

# System information, gathered from platform.uname()
print("="*10,"[System Information]","="*10)
uname=platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Boot time
print("="*10,"[Boot Time]","="*10)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
current_time_timestamp = datetime.now().timestamp()
ts = datetime.fromtimestamp(current_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
print(f"Time Since Boot: {ts.year-bt.year}/{ts.month-bt.month}/{ts.day-bt.day} {ts.hour-bt.hour}:{ts.minute-bt.minute}:{ts.second-bt.second}")

def cpu_info():
    # CPU Information 
    print("="*10,"[CPU INFORMATION]","="*10)
    # Number of Cores
    print("Physical Cores: ", psutil.cpu_count(logical=False))
    print("Total Cores: ", psutil.cpu_count(logical=True))
    # Frequencies
    cpuFreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpuFreq.max:.2f}MHz")
    print(f"Min Frequency: {cpuFreq.min:.2f}MHz")
    print(f"Current Frequency: {cpuFreq.current:.2f}MHz")
    # Usage
    print("CPU Usage per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

cpu_info()
