import socket

msg = b'Hello'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg, ("localhost", 2021))

sock.close()
