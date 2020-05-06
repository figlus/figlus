import socket
import pygame
import pickle
import math
import random
import time

IPADDRES = socket.gethostbyname(socket.gethostname())
PORT = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(IPADDRES)

server.bind((IPADDRES, PORT))
server.listen(2)
cordsArray = [300, 300, 395, 595]  # [xA, xB, ballX, ballY]
paddleSpeed = 7

connection = []
xBallVelocity = 5
yBallVelocity = 5
maxBounceAngle = 8 * math.pi / 12
entryBallSpeed = 5
clock = pygame.time.Clock()


def resetBallPosition(cordsArray):
    global xBallVelocity, yBallVelocity, entryBallSpeed
    cordsArray[2] = 355
    cordsArray[3] = 555
    xBallVelocity = random.choice([-1, 1]) * entryBallSpeed
    yBallVelocity = random.choice([-1, 1]) * entryBallSpeed


def processPositions(cordsArray, paddleAKeyInfo, paddleBKeyInfo):
    global xBallVelocity, yBallVelocity, maxBounceAngle
    global ballSpeed

    #### Paddle Moving ####
    ## Moving paddleA
    if paddleAKeyInfo[0] == True:
        cordsArray[0] -= paddleSpeed
    else:
        cordsArray[0] = cordsArray[0]
    if paddleAKeyInfo[1] == True:
        cordsArray[0] += paddleSpeed
    else:
        cordsArray[0] = cordsArray[0]
    if cordsArray[0] < 0:
        cordsArray[0] = 0
    if cordsArray[0] > 700 - 100:
        cordsArray[0] = 700 - 100
    ## Moving paddleB ##
    if paddleBKeyInfo[0] == True:
        cordsArray[1] -= paddleSpeed
    else:
        cordsArray[1] = cordsArray[1]
    if paddleBKeyInfo[1] == True:
        cordsArray[1] += paddleSpeed
    else:
        cordsArray[1] = cordsArray[1]
    if cordsArray[1] < 0:
        cordsArray[1] = 0
    if cordsArray[1] > 700 - 100:
        cordsArray[1] = 700 - 100
    #### END OF PADDLE MOVING ###

    #### BALL MOVING ####
    cordsArray[2] += xBallVelocity
    cordsArray[3] += yBallVelocity
    if cordsArray[3] < 30 or cordsArray[3] > 790:
        resetBallPosition(cordsArray)

    ## Bouncing ball from vertical walls ##
    if cordsArray[2] <= 0:
        xBallVelocity = -xBallVelocity
    if cordsArray[2] >= 700:
        xBallVelocity = -xBallVelocity

    ## Check if reset button is pressed  - R ##

    #### Paddle and Ball contact detection ####
    ## Detection with paddleA ##
    if cordsArray[3] < (50 + 10) and (cordsArray[2] > cordsArray[0] and cordsArray[2] < cordsArray[0] + 100):
        interSection = cordsArray[2] - cordsArray[0] - 50
        normalizedInterSection = interSection / 50
        angle = normalizedInterSection * maxBounceAngle
        print(math.cos(angle))
        xBallVelocity = xBallVelocity + math.cos(angle)
        yBallVelocity = -yBallVelocity * 1.1

    ## Detection with paddleB ##
    if cordsArray[3] > 750 + 7 and (cordsArray[2] > cordsArray[1] and cordsArray[2] < cordsArray[1] + 100):
        interSection = cordsArray[2] - cordsArray[1] - 50
        normalizedInterSection = interSection / 50
        angle = normalizedInterSection * maxBounceAngle
        print(math.cos(angle))
        xBallVelocity = xBallVelocity + math.cos(angle)
        yBallVelocity = -yBallVelocity * 1.1

    return cordsArray


def waitForConnections():
    while len(connection) < 2:
        conn, addr = server.accept()
        connection.append(conn)
        print(conn)
        print(connection)


def receiveInformations():
    paddleA_Info = pickle.loads(connection[0].recv(1024))
    paddleB_Info = pickle.loads(connection[1].recv(1024))

    return paddleA_Info, paddleB_Info  # assigning whether left or right buttons are pressed or not


while True:
    waitForConnections()

    pickledCordsArray = pickle.dumps(cordsArray)
    # print(pickledCordsArray)
    connection[0].send(pickledCordsArray)
    connection[1].send(pickledCordsArray)

    paddleAKeyInfo, paddleBKeyInfo = receiveInformations()

    cordsArray = processPositions(cordsArray, paddleAKeyInfo, paddleBKeyInfo)
    clock.tick(60)