import pygame
from paddle import Paddle
from ball import Ball

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Open new window
gameWidth = 700;   gameHeight = 1000
size = (gameWidth, gameHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")






carryOn = True
clock = pygame.time.Clock()

### Creating game elements ###
paddleA = Paddle(WHITE,100,10)
paddleA.rect.x = 300
paddleA.rect.y = 50

paddleB = Paddle(WHITE,100,10)
paddleB.rect.x=300
paddleB.rect.y=1000-50

ball = Ball(WHITE,6,6)
ball.rect.x = 365
ball.rect.y = 495

lastPaddleAMove = 2 # 0 stands for left | 1 stands for right
lastPaddleBMove = 2 # 0 stands for left | 1 stands for right

### Creating list for al spirtes and adding them ###
all_sprites_list=pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)










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


    if keys[pygame.K_a]:
        paddleA.moveLeft(5)
        lastPaddleAMove = 0
    if keys[pygame.K_d]:
        paddleA.moveRight(5)
        lastPaddleAMove = 1
    if keys[pygame.K_LEFT]:
        paddleB.moveLeft(5)
        lastPaddleBMove = 0
    if keys[pygame.K_RIGHT]:
        paddleB.moveRight(5)
        lastPaddleBMove = 1

    ### Space for game logic ###
    all_sprites_list.update()
    ball.wallBounce()
    ball.resetBall()


    # Checking for collisions with paddles
    if pygame.sprite.collide_mask(ball,paddleA):
        interSecX = ball.rect.x - paddleA.rect.x - 50
        ball.paddleBounce(interSecX)

    if pygame.sprite.collide_mask(ball, paddleB):
        interSecX = ball.rect.x - paddleB.rect.x - 50
        ball.paddleBounce(interSecX)


    ### Space for drawing code ###
    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,[0,495],[700,495],5)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()






