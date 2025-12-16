from Player import *
import pygame
import sys

playercolor = (22, 76, 6)

pygame.init()

player = Player(10, 0, 0, 40, 40, playercolor)

width = 1200
height = 600
running = True

groundheight = 200

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("ProtienSmoothie")
skycolor = (186, 181, 180)

gravity = 0.4
speed = 1
jump = 40

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    player.y += gravity

    if player.y > (height - groundheight - player.height):
        player.y = (height - groundheight - player.height)

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
                 player.y -= jump


    if player.x > width - player.width:
         player.x = width - player.width
    if player.x < 0:
         player.x = 0

    screen.fill(skycolor)

    pygame.draw.rect(screen, (107, 14, 97), (0, (height - groundheight), width, groundheight), 0)
    pygame.draw.rect(screen, (player.color), (player.x, player.y, player.width, player.height), 0)
    pygame.display.flip()


pygame.quit()
sys.exit()