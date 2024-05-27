import pygame
import random
import math
import constants as c

pygame.init()
clock = pygame.time.Clock()
player = pygame.rect.Rect(c.WIDTH/2,c.HEIGHT/2,c.PLAYER_WIDTH,c.PLAYER_HEIGHT)
platform = pygame.rect.Rect(200,200,100,30)
window = pygame.display.set_mode((1300,680))

vel_x, vel_y = 5,5
jumping = False
jump_count = 0

def main():
    global jumping
    running = True
    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        if keys[pygame]:
            pass
        else:
            player.y += vel_y
            player.y += vel_y
        if keys[pygame.K_a]:
            player.x -= vel_x
        if keys[pygame.K_d]:
            player.x += vel_x
        
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumping = True
        jump() 
        check_y()
        draw()
def check_y():
    while True:
        if player.bottom > c.HEIGHT:
            player.y -= 1
        elif platform.colliderect(player):
            player.y -= 1
        else:
            break

def jump():   
    global jumping, jump_count, vel_y
    if jumping and jump_count < 20:
        vel_y = -5
        jump_count += 1
    else: 
        vel_y = 5
        jump_count = 0
        jumping = False

def draw():
    global window
    window.fill("white")
    pygame.draw.rect(window, "black", platform)
    pygame.draw.rect(window, "blue", player)
    pygame.display.update() 


if __name__ == "__main__":
    main()
