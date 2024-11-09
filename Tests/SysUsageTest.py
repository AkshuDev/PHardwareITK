import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from phardwareitk.System import SysUsage

#Note: Some funcs not included as they are not supported by our testing OS. Testing OS -> Windows 11
# If you like please test them, and give response to our github

# CPU Section
print("Logical CPU Count: ", SysUsage.System.CpuCount(True))
print("Physical CPU Count: ", SysUsage.System.CpuCount(False))

print("CPU Usage: ", SysUsage.System.CpuUsage())
print("CPU Usage Details: ", SysUsage.System.CpuUsageDetails())
print("CPU Usage Times Details: ", SysUsage.System.CpuUsageTimesDetails())

print("CPU Stats: ", SysUsage.System.CpuStats())
print("CPU Frequency: ", SysUsage.System.CpuFreq())
print("CPU Frequency Per Core: ", SysUsage.System.CpuFreqPerCore())
print("CPU Load Average (1, 5, 15 minutes): ", SysUsage.System.CpuLoadAvg())
print("CPU Affinity (current process): ", SysUsage.System.CpuAffinity())
print("CPU Times Per Core: ", SysUsage.System.CpuTimesPerCore())
print("CPU Usage Per Core: ", SysUsage.System.CpuUsagePerCore())

# Battery Section
print("Battery Status: ", SysUsage.System.SystemBatteryStatus())
print("Battery Percentage: ", SysUsage.System.SystemBatteryPercentage())
print("Battery Time Left: ", SysUsage.System.SystemBatteryTimeLeft())
print("Battery Plugged: ", SysUsage.System.SystemBatteryPlugged())
print("Battery Seconds Left: ", SysUsage.System.SystemBatterySecsLeft())
print("Battery Plugged Time: ", SysUsage.System.SystemBatteryPluggedTime())
print("Battery Is Charging: ", SysUsage.System.SystemBatteryIsCharging())
print("Battery Time to Full Charge: ", SysUsage.System.SystemBatteryTimeToFullCharge())
print("Battery Details: ", SysUsage.System.SystemBatteryDetails())
print("Battery Status Details: ", SysUsage.System.SystemBatteryStatusDetails())
print("Battery Type: ", SysUsage.System.SystemBatteryType())

# Disk Section
print("Disk Usage (/): ", SysUsage.System.DiskUsage('/'))
print("Disk Partitions: ", SysUsage.System.DiskPartitions())
print("Disk Free Space (/): ", SysUsage.System.DiskFree('/'))
print("Disk Used Space (/): ", SysUsage.System.DiskUsed('/'))
print("Disk Total Space (/): ", SysUsage.System.DiskTotal('/'))
print("Disk Read Bytes: ", SysUsage.System.DiskReadBytes())
print("Disk Write Bytes: ", SysUsage.System.DiskWriteBytes())
print("Disk Reads: ", SysUsage.System.DiskReads())
print("Disk Writes: ", SysUsage.System.DiskWrites())
print("Disk Read Time: ", SysUsage.System.DiskReadTime())
print("Disk Write Time: ", SysUsage.System.DiskWriteTime())
print("Disk I/O Merges: ", SysUsage.System.DiskIOMerges())
print("Disk Queue Depth: ", SysUsage.System.DiskQueueDepth())

# Memory Section
print("RAM Info: ", SysUsage.System.RAMInfo())
print("Total RAM: ", SysUsage.System.RAMTotal())
print("Available RAM: ", SysUsage.System.RAMAvailable())
print("Used RAM: ", SysUsage.System.RAMUsed())
print("RAM Usage Percentage: ", SysUsage.System.RAMPercent())
print("Active RAM: ", SysUsage.System.RAMActive())
print("Buffered RAM: ", SysUsage.System.RAMBuffered())
print("Shared RAM: ", SysUsage.System.RAMShared())
print("Slab Memory: ", SysUsage.System.RAMSlab())
print("Free RAM: ", SysUsage.System.RAMFree())

print("RAM Used By Processes: ", SysUsage.System.RAMUsedByProcesses())
print("RAM Swap Total: ", SysUsage.System.RAMSwapTotal())
print("RAM Swap Used: ", SysUsage.System.RAMSwapUsed())
print("RAM Swap Free: ", SysUsage.System.RAMSwapFree())
print("RAM Swap Percentage: ", SysUsage.System.RAMSwapPercent())
print("RAM Swap In Use: ", SysUsage.System.RAMSwapInUse())
print("RAM Buffer Info: ", SysUsage.System.RAMBufferInfo())
print("Total Physical RAM: ", SysUsage.System.RAMPhysicalMemory())

# Replace '1234' with your actual process ID if needed
print("RAM Used by Process 1234: ", SysUsage.System.RAMActiveProcessMemory(1234))

# Network Section
print("Network Interfaces: ", SysUsage.System.Interfaces())
print("Network Interface Stats: ", SysUsage.System.InterfaceStats())

print("Network Connections (inet): ", SysUsage.System.NetworkConnections('inet'))
print("Network Stats: ", SysUsage.System.NetworkStats())

# Replace 'eth0' with your actual interface name (e.g., 'wlan0', 'en0', etc.)
print("Interface Network Stats (eth0): ", SysUsage.System.InterfaceNetworkStats('eth0'))

print("Default Gateway: ", SysUsage.System.DefaultGateway())
print("DNS Config: ", SysUsage.System.DNSConfig())

# Replace 'eth0' with your actual interface name
print("IP Address of eth0: ", SysUsage.System.IPAddress('eth0'))
print("MAC Address of eth0: ", SysUsage.System.MACAddress('eth0'))

print("Hostname: ", SysUsage.System.Hostname())
print("FQDN: ", SysUsage.System.FQDN())
print("Local IP Address: ", SysUsage.System.LocalIPAddress())

# Replace 'eth0' with your actual interface name
print("Interface State (eth0): ", SysUsage.System.InterfaceState('eth0'))
print("Is Interface Up (eth0): ", SysUsage.System.IsInterfaceUp('eth0'))

# Replace '1234' with your actual process ID
print("Network Connections by PID (1234): ", SysUsage.System.NetworkConnectionsByPID(1234))

print("Local Ports In Use: ", SysUsage.System.LocalPortsInUse())
print("External IP Address: ", SysUsage.System.ExternalIPAddress())

# Replace 'eth0' with your actual interface name
print("Interface Type (eth0): ", SysUsage.System.InterfaceType('eth0'))

# Replace 'psutil.sconn' with an actual connection object if you have one
print("Connection Status: ", SysUsage.System.ConnectionStatus(None))  # Requires a valid connection object

# Replace 'eth0' with your actual interface name
print("Netmask of eth0: ", SysUsage.System.Netmask('eth0'))