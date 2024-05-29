import pygame
import constants as c

class Entity(pygame.sprite.Sprite):

    dist_to_plr: int
    rect: pygame.rect.Rect
    ref_rect: pygame.rect.Rect
    scale: int

    def __init__(self, rect, dist_to_player, groups):
        self.dist_to_plr = dist_to_player
        self.rect = rect
        self.ref_rect = rect
        self.update_scale()
        super().__init__(groups)

    def update_scale(self):
        # BUG: Center location changes when scalling, need to find this location based of the location relative to the ceneter vetical
        self.scale = (c.RENDER_DIST - self.dist_to_plr) * c.SCALE_FACTOR
        self.rect = pygame.rect.Rect(self.ref_rect.x * self.scale,
                                     self.ref_rect.y - ((self.ref_rect.h * self.scale)//2),
                                     self.ref_rect.w * self.scale,
                                     self.ref_rect.h * self.scale)

    def strafe(self, dist):
        self.rect.x += dist * self.scale
        self.ref_rect.x += dist

    def draw(self, surface):
        pygame.draw.rect(surface,"black",(self.rect.x + c.WIDTH//2, self.rect.y, self.rect.w, self.rect.h))

    def update(self, *args, **kwargs):
        if args[0] == "walk":
            self.dist_to_plr += args[1]
            self.update_scale()
        elif args[0] == "strafe":
            self.strafe(args[1])
        elif args[0] == "draw":
            self.draw(args[1])
        

