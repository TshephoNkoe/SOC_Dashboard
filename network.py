import psutil
import socket

# Function to monitor network traffic (bytes sent and received)
def monitor_network_traffic():
    """
    Monitors network traffic and returns the bytes sent and received on the machine.
    """
    network_stats = psutil.net_io_counters()
    return {"bytes_sent": network_stats.bytes_sent, "bytes_recv": network_stats.bytes_recv}

# Function to scan for open ports on a given IP address
def check_open_ports(target_ip):
    """
    Scans for open ports on the specified target IP address in the range from 20 to 1023.
    Returns a list of open ports.
    """
    open_ports = []
    for port in range(20, 1024):  # Scanning common ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, port))  # Try to connect to each port
        if result == 0:  # Port is open
            open_ports.append(port)
        sock.close()
    return open_ports
