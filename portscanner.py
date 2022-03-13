import sys
import socket
import threading

usage = "python3 try_portscanner.py TARGET START_PORT END_PORT "

if (len(sys.argv)) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Host is not active")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    conn = sock.connect_ex((target, port))
    if (not conn):
        print("Port {} is Open".format(port))
    sock.close()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
