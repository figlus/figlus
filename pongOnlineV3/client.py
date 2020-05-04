import pygame
import pickle
import socket
import time

pygame.init()

# Creating client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IPADDR = "192.168.1.66" #socket.gethostbyname(socket.gethostname())
PORT = 5555
client.connect((IPADDR, PORT))
# Creating general variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DISPLAY_HEIGHT = 1000
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
    data = client.recv(2048)
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
        drawPaddles(positionsData[1], 940, 1)
        drawBall(positionsData[2], positionsData[3])
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

        pickledKeyArray = pickle.dumps(keyArray)
        client.send(pickledKeyArray)











display()