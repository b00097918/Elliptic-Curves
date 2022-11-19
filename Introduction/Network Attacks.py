#Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.

#Python makes such network communication easy with the telnetlib module. Conveniently, it's part of Python's standard library, so let's use it for now.

#For this challenge, connect to socket.cryptohack.org on port 11112. Send a JSON object with the key buy and value flag.

#The example script below contains the beginnings of a solution for you to modify, and you can reuse it for later challenges.

#Connect at nc socket.cryptohack.org 11112

#Challenge files:
#  - telnetlib_example.py

#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "flag" #Simply change from clothes to flag and this will give us the flag for the cryptohack
}
json_send(request)

response = json_recv()

print(response)



