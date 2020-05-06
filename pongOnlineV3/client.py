import pygame
import pickle
import socket
import time

pygame.init()

# Creating client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IPADDR = "34.89.181.232" #socket.gethostbyname(socket.gethostname())
PORT = 5555
client.connect((IPADDR, PORT))
# Creating general variables

WHITE = (255, 255, 255)
GREY = (179,179,179)
BLACK = (102,102,102)
DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 700

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("PONG")

#

def drawPaddles(xPos,yPos,player):
    if player == 0:
        pygame.draw.rect(gameDisplay, WHITE, [xPos, yPos, 100, 10])
    if player == 1:
        pygame.draw.rect(gameDisplay, WHITE, [xPos, yPos, 100, 10])

def drawBall(xPos, yPos):
    pygame.draw.rect(gameDisplay, WHITE, [xPos, yPos,7,7])

def receiveData():
    data = client.recv(100)
    data = pickle.loads(data)

    return data

def display():
    carryOn = True
    key_left = False
    key_right = False
    while carryOn == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        positionsData = receiveData()   #receiving coorinates [xA, xB, ballX, ballY]
        gameDisplay.fill(BLACK)
        drawPaddles(positionsData[0], 50, 0)
        drawPaddles(positionsData[1], 750, 1)
        drawBall(positionsData[2], positionsData[3])

        pygame.display.flip()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_left = True
                if event.key == pygame.K_RIGHT:
                    key_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key_left = False
                if event.key == pygame.K_RIGHT:
                    key_right = False

        keyArray = [key_left, key_right]

        pickledKeyArray = pickle.dumps(keyArray,2)
        client.sendall(pickledKeyArray)












display()