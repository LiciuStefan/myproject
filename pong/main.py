import pygame
import random
import math

pygame.init()
HEIGHT = 500
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")

icon = pygame.image.load('beer-pong.png')
pygame.display.set_icon(icon)


#player1:
player1Img= pygame.image.load('player1.png')
player1X = -23
player1Y = 255
player1Y_change = 0

def player1(x,y):
    screen.blit(player1Img, (x, y))

#player2:
player2Img= pygame.image.load('player2.png')
player2X = 560
player2Y = 0
player2Y_change = 0

#ball:
ballImg = pygame.image.load('medicine-ball.png')
ballX = random.randint(100, 400)
ballY = random. randint(100, 400)
ballX_change = random.choice([-0.5, 0.5])
ballY_change = random.choice([-0.5, 0.5])

def ball(x, y):
    screen.blit(ballImg, (x,y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

#collision:
def isCol(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1-x2,2)+math.pow(y1-y2,2)))
    distance2 = math.sqrt((math.pow(x1 - x2, 2) + math.pow(y1 - y2-64, 2)))
    if distance <30 or distance2 <30:
        return True
    return False

#score:
score1_value = 0
score2_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text1X = 10
text1Y = 10
text2X = 400
def show_score(x,y,value):
    score = font.render("Score: " + str(value), True, (255,255,255))
    screen.blit(score, (x,y))

#game over:
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over = font.render("GAME OVER",True, (255,255,255))
    screen.blit(over, (200,250))

running = True
while running:
    screen.fill((142,79,79))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2Y_change = -1.2
            if event.key == pygame.K_DOWN:
                player2Y_change = 1.2
            if event.key == pygame.K_w:
                player1Y_change = -1.2
            if event.key == pygame.K_s:
                player1Y_change = 1.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2Y_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1Y_change = 0

    collision1 = isCol(ballX, ballY, player1X, player1Y)
    collision2 = isCol(ballX, ballY, player2X, player2Y)
    if collision1 or collision2:
        if ballX_change < 0:
         ballX_change = -ballX_change +0.01
        else:
         ballX_change = -ballX_change -0.01
        if ballY_change < 0:
         ballY_change = -ballY_change + 0.01
        else:
         ballY_change = -ballY_change - 0.01



    player1Y += player1Y_change
    player2Y += player2Y_change
    player1(player1X, player1Y)
    player2(player2X, player2Y)

    if player1Y <= 0:
        player1Y = 0
    elif player1Y >=440:
        player1Y = 440
    if player2Y <= 0:
        player2Y = 0
    elif player2Y >=440:
        player2Y = 440

    ball(ballX, ballY)
    ballX += ballX_change
    ballY += ballY_change

    if ballY <= 0 or ballY >= 468:
        ballY_change = -ballY_change
    if ballY>=0 and ballY <= 600:
     if ballX < -30:
        score2_value +=1
        ballX = random.randint(290, 310)
        ballY = random.randint(100, 400)
        ballX_change = random.choice([-0.5, 0.5])
        ballY_change = random.choice([-0.5, 0.5])

     elif ballX > 570:
        score1_value +=1
        ballX = random.randint(290, 310)
        ballY = random.randint(100, 400)
        ballX_change = random.choice([-0.5, 0.5])
        ballY_change = random.choice([-0.5, 0.5])

    show_score(text1X, text1Y, score1_value)
    show_score(text2X, text1Y, score2_value)

    if score1_value >= 5 or score2_value >= 5:
      ballY = 2000
      game_over_text()


    pygame.display.update()