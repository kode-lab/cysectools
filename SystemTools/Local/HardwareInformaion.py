# Kode Blue, 10/29/2020
# Script for finding Hardware Informaiton about a machine

import platform
import psutil
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Scale bytes to Human-Readable format
    """
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_information():
    # System information, gathered from platform.uname()
    print("="*20,"[System Information]","="*20)
    uname=platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def boot_time():
    # Boot time
    print("="*20,"[Boot Time]","="*20)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    current_time_timestamp = datetime.now().timestamp()
    ts = datetime.fromtimestamp(current_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    print(f"Time Since Boot: {ts.year-bt.year}/{ts.month-bt.month}/{ts.day-bt.day} {ts.hour-bt.hour}:{ts.minute-bt.minute}:{ts.second-bt.second}")

def cpu_info():
    # CPU Information 
    print("="*20,"[CPU INFORMATION]","="*20)
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

def mem_info():
    # Memory (RAM) informaiton
    print("="*20,"[Memory Information]","="*20)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    # Swap details (if there is any)
    print("="*5,"[SWAP]","="*5)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")
    
def disk_info():
    print("="*20,"[Disk Information]","="*20)
    print("Partitions and Usage:")
    # Get Disk Paritions
    parts = psutil.disk_partitions()
    for part in parts:
        print(f"=== Device: {part.device} ===")
        print(f"    Mountpoint: {part.mountpoint}")
        print(f"    File System Type: {part.fstype}")
        try:
            partition_usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            # the disk isn't ready, nbd
            continue
        print(f"    Total Size: {get_size(partition_usage.total)}")
        print(f"    Used: {get_size(partition_usage.used)}")
        print(f"    Free: {get_size(partition_usage.free)}")
        print(f"    Percentage: {partition_usage.percent}%")
    
    # Get IO stats since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total Write: {get_size(disk_io.write_bytes)}")

def net_info():
    # Network Information
    print("="*20,"[Network Information]","="*20)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"    IP Address:    {address.address}")
                print(f"    Netmask:       {address.netmask}")
                print(f"    Broadcast IP:  {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"    MAC Address:   {address.address}")
                print(f"    Netmask:       {address.address}")
                print(f"    Broadcast MAC: {address.address}")
    # Get IO stats since Boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Recieved: {get_size(net_io.bytes_recv)}")

def main():
        system_information()
        boot_time()
        cpu_info()
        mem_info()
        disk_info()
        net_info()

main()
# Still figuring out args parse 
#if __name__ == "__main__":
#    import argparse
#    parser = argparse.ArgumentParser(description="Gather Information about a system")
#    parser.add_argument("-s", "--system-information", help="Display System Information")
#    parser.add_argument("-b", "--boot-time", help="Display Boot Time")
#    parser.add_argument("-c", "--cpu-info", help="Display CPU Information and Usage")
#    parser.add_argument("-m", "--mem-info", help="Display Memory Informaiton and Usage")
#    parser.add_argument("-d", "--disk-info", help="Display Disk Information and Usage")
#    parser.add_argument("-n", "--network-info", help="Display Network Information and Usage")
