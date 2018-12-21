from bluetooth import *
import sys


def __init__(self):
    addr = "AC:9A:22:91:67:58"
    print("Searching for SampleServer on %s" % addr)
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)

sock.close()