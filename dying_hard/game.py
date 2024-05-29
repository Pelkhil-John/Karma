import pygame
import random
import math
import constants as c
import entity

pygame.init()
font = pygame.font.SysFont("Calibri", 50)
clock = pygame.time.Clock()
right_hand = pygame.rect.Rect(c.RIGHT_HAND_REST_POS,(c.PLAYER_WIDTH,c.PLAYER_HEIGHT))
right_hand_alpha = 255
left_hand = pygame.rect.Rect(c.LEFT_HAND_REST_POS,(c.PLAYER_WIDTH,c.PLAYER_HEIGHT))
left_hand_alpha = 255
energy: int
max_energy = 100
ents = pygame.sprite.Group()


window = pygame.display.set_mode((1300,680), pygame.SRCALPHA)

vel_x, vel_y = 5,5
energy = 100

def main():
    global right_hand_alpha, left_hand_alpha, energy
    running = True
    while running:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        if keys[pygame.K_w]:
            ents.update("walk", -10)
        if keys[pygame.K_s]:
            ents.update("walk", 10)
        if keys[pygame.K_a]:
            ents.update("strafe", 10)
        if keys[pygame.K_d]:
            ents.update("strafe", -10)

        # RIGHT HAND RETURN
        if mouse_pressed[2] and energy > 0:
            right_hand.center = mouse_pos
            right_hand_alpha = 255
            energy -= 1
        elif not right_hand.collidepoint((1000, 550)):
            if right_hand.centerx > 1000:
                right_hand.centerx -= 1
            else:
                right_hand.centerx += 1
            if right_hand.centery > 550:
                right_hand.centery -= 1
            else:
                right_hand.centery += 1
        elif right_hand_alpha -2 > 0:
            right_hand_alpha -=2
        else: 
            right_hand_alpha = 0
        
        # LEFT HAND RETURN
        if mouse_pressed[0] and energy > 0:
            left_hand.center = mouse_pos
            left_hand_alpha = 255
            energy -= 1
        elif not left_hand.collidepoint((200, 550)):
            if left_hand.centerx > 200:
                left_hand.centerx -= 1
            else:
                left_hand.centerx += 1
            if left_hand.centery > 550:
                left_hand.centery -= 1
            else:
                left_hand.centery += 1
        elif left_hand_alpha -2 > 0:
            left_hand_alpha -=2
        else: 
            left_hand_alpha = 0
            

        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
        draw()

def draw():
    global window
    window.fill("white")
    window.blit(get_alpha_rect_surface(right_hand, (0,0,255,right_hand_alpha)),(right_hand.topleft))
    window.blit(get_alpha_rect_surface(left_hand, (0,0,255,left_hand_alpha)),(left_hand.topleft))
    pygame.draw.rect(window, "green", (0,0,energy*4,50))
    window.blit(font.render(f"{energy}/{max_energy}",False,(0,0,0)),(0,0))
    ents.update("draw", window)
    pygame.display.update() 

def get_alpha_rect_surface(rect: pygame.rect.Rect, color, radius = -1) -> pygame.Surface:
    surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(surface, color, surface.get_rect(), border_radius=radius)
    return surface


def settup():
    for _ in range(10):
        entity.Entity(pygame.Rect(random.randint(0 + c.PLAYER_WIDTH, c.WIDTH - c.PLAYER_WIDTH), c.HEIGHT//2 - 32, 64,64), 
                      random.randint(c.RENDER_DIST//10,c.RENDER_DIST), ents)

if __name__ == "__main__":
    settup()
    main()
