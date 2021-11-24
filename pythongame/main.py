import pygame
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

playerImg = pygame.image.load('player.png')
playerX = 368
playerY = 500
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('asteroid.png')
enemyX = random.randint(0, 764)
enemyY = 0
enemyX_change = 0
enemyY_change = 0.3
enemyY_col_change = 0.1
number_of_enemies = 0
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


pygame.display.set_caption("Space invaders")
icon = pygame.image.load('space-gun.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('space-galaxy-background.png')

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (300,250))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+20, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    return False


running = True
while running:
    screen.fill((114, 67, 114))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                 bulletX = playerX
                 bulletY = playerY
                 fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_UP:
                playerY_change = -0.7
            if event.key == pygame.K_DOWN:
                playerY_change = +0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= -32:
        playerX = 768
    elif playerX >= 768:
        playerX = 0
    if playerY < 400:
        playerY = 400
    elif playerY > 500 :
        playerY = 500

    enemyY += enemyY_change
    if enemyY > 500:
        enemyY = 0
        enemyX = random.randint(0, 764)
        number_of_enemies += 1

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state ="ready"
        enemyY = 0
        enemyX = random.randint(0, 764)
        score_value +=1
        if score_value % 2 == 0:
         enemyY_change += enemyY_col_change
    show_score(textX, textY)
    if number_of_enemies >2:
         enemyX = 2000
         game_over_text()



    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
