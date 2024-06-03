import pygame

import constants as c

class Player(pygame.sprite.Sprite):

    right_hand = pygame.rect.Rect(c.RIGHT_HAND_REST_POS, (c.HAND_SIZE,c.HAND_SIZE))
    right_hand_alpha = 255
    right_hand_surf: pygame.surface.Surface
    left_hand = pygame.rect.Rect(c.LEFT_HAND_REST_POS,(c.PLAYER_WIDTH,c.PLAYER_HEIGHT))
    left_hand_alpha = 255
    left_hand_surf: pygame.surface.Surface

    energy = 100
    max_energy = 100
    
    # ideas: states should be stored as ints which can be referenced by their const name
    # IDLE = 0
    # RUNNING = 1
    # JUMPING = 2
    # LANDING = 3


    def __init__(self, group=[], x=0, y=0):
        self.import_sprites()
        super().__init__(group)


    def import_sprites(self):
        self.right_hand_surf = pygame.transform.scale(pygame.image.load("Karma/dying_hard/imgs/The_Hand.png").convert_alpha(), self.right_hand.size)
        self.left_hand_surf = pygame.transform.flip(self.right_hand_surf.copy(),True,False)


    def update(self, *args, **kwargs):
        if args[0] == "tick":
            self.tick()

    def tick():
        pass

    