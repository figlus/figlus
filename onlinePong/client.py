import pygame
from paddle import Paddle
from network import Network
#Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Open new window
gameWidth = 700;   gameHeight = 1000
size = (gameWidth, gameHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


n = Network()
startPos = read_pos(n.getPos())
carryOn = True
clock = pygame.time.Clock()

paddleA = Paddle(WHITE,100,10)
paddleA.rect.x = startPos[0]
paddleA.rect.y = startPos[1]

paddleB = Paddle(WHITE,100,10)
paddleB.rect.x=300
paddleB.rect.y=1000-40

### Creating list for al spirtes and adding them ###
all_sprites_list=pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)









### Main Loop ###
while carryOn==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False

    ### Moving the paddles when keys are pressed ###
    keys=pygame.key.get_pressed()

    ##Onle the A-D keys are responding !
    if keys[pygame.K_a]:
        paddleA.moveLeft(5)
    if keys[pygame.K_d]:
        paddleA.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddleA.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddleA.moveRight(5)
    ### Space for game logic ###
    all_sprites_list.update()


    ### Space for communication with server ###
    p2Pos = read_pos(n.send(make_pos((paddleA.rect.x,paddleA.rect.y))))
    paddleB.rect.x=p2Pos[0]
    paddleB.rect.y=p2Pos[1]



    ### Space for drawing code ###
    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,[0,495],[700,495],5)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()






