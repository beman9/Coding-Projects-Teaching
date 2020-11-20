import pygame
from pygame import mixer
import random
import math

# initializes PyGame
pygame.init()

# create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# create the background
background = pygame.image.load('space.png')
background = pygame.transform.scale(background, (800, 600))

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ghost.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Projectile
# 'ready' = laser is ready to fire
# 'fire' = laser is in motion
projectileImg = pygame.image.load('projectile.png')
projectileX = 0
projectileY = 480
projectileX_change = 0
projectileY_change = 10
projectile_state = 'ready'

# Define score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)




def showScore(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))


def player(x, y):
    # blit draws the image to the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_projectile(x, y):
    global projectile_state
    projectile_state = 'fire'
    screen.blit(projectileImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, projectileX, projectileY):
    distance = math.sqrt((math.pow(enemyX - projectileX, 2)) + (math.pow(enemyY - projectileY, 2)))
    if distance < 30:
        return True
    else:
        return False


# Game loop
pygame.key.set_repeat(10, 10)
running = True
while running:

    # RGB = (0 - 255 for each value)
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if projectile_state == 'ready':
                    # Create and play laser sound
                    projectile_sound = mixer.Sound('laser.wav')
                    projectile_sound.play()
                    # get X-coordinate of player and put projectile there
                    fire_projectile(playerX, projectileY)
                    projectileX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    # keeping player within the bounds of the screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # keeping enemy within bounds of the screen
    enemyX += enemyX_change

    # enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], projectileX, projectileY)
        if collision:
            # Create and play explosion sound
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()

            projectileY = 480
            projectile_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    # Projectile movement
    if projectileY <= 0:
        projectileY = 480
        projectile_state = 'ready'

    if projectile_state == 'fire':
        fire_projectile(projectileX, projectileY)
        projectileY -= projectileY_change

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
