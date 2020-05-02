import socket
from _thread import *
import sys

server=socket.gethostbyname(socket.gethostname());
port = 5555

# AF_INET stands for IPv4 and the socket.SOCK_STREAM stands for TCP, continous stream
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding our socket to host server and the specific port
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(300,50),(300,950)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data



            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]

                if player == 0:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    # conn is another socket object but on the side of a client
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
