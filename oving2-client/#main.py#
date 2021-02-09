# Copyright (C) 2021 Joakim Skogø Langvand

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket, select, sys

#  TODO: Structure

UDP_ADDR = '127.0.0.1'
UDP_PORT = 2021 #  TODO: Override port with argument
MAX_LENGTH = 128

BUFFER_SIZE = 1024

greeting = "RemoteCalc UDP client v1.0-ALPHA\n"

print(greeting)

def send(msg):
    s.sendto(msg.encode("utf-8") + b'\n', (UDP_ADDR, UDP_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 2020))
s.settimeout(2)

response = b''

msg = input("> ")

while msg != "exit":
    send(msg)

    try:
        data, addr = s.recvfrom(128)
        print("ans: {}".format(data.decode("utf-8")))

    except socket.timeout:
        print("Request timed out")
        
    msg = input("> ")

#  Tell the server we're done
send("bye")

#  Clean up
s.close()

sys.exit(0)
