import pygame
import random
import constants as c
import player
import entity

clock:pygame.time.Clock
ents: pygame.sprite.Group
p: player.Player

vel_x, vel_y = 5,5

def main():
    running = True
    while running:
        clock.tick(c.FPS)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        if keys[pygame.K_w]:
            ents.update("walk", -2)
        if keys[pygame.K_s]:
            ents.update("walk", 2)
        if keys[pygame.K_a]:
            ents.update("strafe", 10)
        if keys[pygame.K_d]:
            ents.update("strafe", -10)

        # RIGHT HAND RETURN
        if mouse_pressed[2] and p.energy > 0:
            p.right_hand.center = mouse_pos
            p.right_hand_alpha = 255
            p.energy -= 1
        elif not p.right_hand.collidepoint(c.RIGHT_HAND_REST_POS):
            if p.right_hand.centerx > c.RIGHT_HAND_REST_POS[0]:
                p.right_hand.centerx -= 1
            else:
                p.right_hand.centerx += 1
            if p.right_hand.centery > c.RIGHT_HAND_REST_POS[1]:
                p.right_hand.centery -= 1
            else:
                p.right_hand.centery += 1
        elif p.right_hand_alpha -2 > 0:
            p.right_hand_alpha -=2
        else: 
            p.right_hand_alpha = 0
        
        # LEFT HAND RETURN
        if mouse_pressed[0] and p.energy > 0:
            p.left_hand.center = mouse_pos
            p.left_hand_alpha = 255
            p.energy -= 1
        elif not p.left_hand.collidepoint(c.LEFT_HAND_REST_POS):
            if p.left_hand.centerx > c.LEFT_HAND_REST_POS[0]:
                p.left_hand.centerx -= 1
            else:
                p.left_hand.centerx += 1
            if p.left_hand.centery > c.LEFT_HAND_REST_POS[1]:
                p.left_hand.centery -= 1
            else:
                p.left_hand.centery += 1
        elif p.left_hand_alpha -2 > 0:
            p.left_hand_alpha -=2
        else: 
            p.left_hand_alpha = 0
            

        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
        draw()

def draw():
    window.fill("white")
    pygame.draw.rect(window, "green", (0,0,p.energy*4,50))
    window.blit(c.FONT.render(f"{p.energy}/{p.max_energy}",False,(0,0,0)),(0,0))
    ents.update("draw", window)
    window.blit(p.right_hand_surf, p.right_hand.topleft)
    window.blit(p.left_hand_surf, p.left_hand.topleft)
    pygame.display.update() 


def get_alpha_rect_surface(rect: pygame.rect.Rect, color, radius = -1) -> pygame.Surface:
    surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(surface, color, surface.get_rect(), border_radius=radius)
    return surface


def settup():
    global p
    c.settup()
    p = player.Player()
    for _ in range(10):
        entity.Entity(pygame.Rect(random.randint(0 + c.PLAYER_WIDTH, c.WIDTH - c.PLAYER_WIDTH), c.HEIGHT//2 - 32, 64,64), 
                      random.randint(c.RENDER_DIST//10,c.RENDER_DIST), ents)


def make_groups():
    global ents
    ents = pygame.sprite.Group()


def start_up():
    global clock, window
    pygame.init()
    window = pygame.display.set_mode((c.WIDTH,c.HEIGHT), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    #HANDLES PATHING
    make_groups()


if __name__ == "__main__":
    start_up()
    settup()
    main()
