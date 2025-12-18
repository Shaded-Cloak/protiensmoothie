from Player import *
import pygame
import sys
import random

playercolor = (22, 76, 6)

zombies = []

pygame.init()

def addzombie(amount = 1):
     for i in range(amount):
        zombies.append(Entity(2, random.randint(0, 1200), 0, 40, 40, (36, 24, 43)))

player = Player(10, 0, 0, 40, 40, playercolor)

width = 1200
height = 600
running = True

groundheight = 200

addzombie(3)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("ProtienSmoothie")
skycolor = (186, 181, 180)

gravity = 0.1
zombiegravity = 0.3
speed = 1
jump = 5

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    player.velocity += gravity

    if player.y > (height - groundheight - player.height):
        player.y = (height - groundheight - player.height)
        player.velocity = 0

    keys = pygame.key.get_pressed()
    for key_code, pressed in enumerate(keys):
            if pressed:
                 print(key_code)
                 print(pressed)
            if pressed and key_code == 4:
                player.x-= speed
            elif pressed and key_code == 7:
                player.x += speed
            elif pressed and key_code == 26 and player.y == height - groundheight - player.height:
                 player.velocity = -jump

    for i in zombies:
         i.y += zombiegravity

         if i.y > (height - groundheight - i.height):
            i.y = (height - groundheight - i.height)

    if player.x > width - player.width:
         player.x = width - player.width
    if player.x < 0:
         player.x = 0

    player.y += player.velocity

    

    screen.fill(skycolor)

    pygame.draw.rect(screen, (107, 14, 97), (0, (height - groundheight), width, groundheight), 0)
    pygame.draw.rect(screen, (player.color), (player.x, player.y, player.width, player.height), 0)
    for i in zombies:
         pygame.draw.rect(screen, (i.color), (i.x, i.y, i.width, i.height), 0)
    pygame.display.flip()


pygame.quit()
sys.exit()