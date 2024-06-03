import pygame
import math
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
        """ finds the relative scale of the object based on its distance to the player, then scales the size of the entity to match
        
        """
        # BUG: Center location changes when scalling, need to find this location based of the location relative to the ceneter vetical
        self.scale = math.tan(math.atan(self.ref_rect.h / self.dist_to_plr))
        self.rect = pygame.rect.Rect(self.ref_rect.x * self.scale,
                                     self.ref_rect.y - ((self.ref_rect.h * self.scale)//2),
                                     self.ref_rect.w * self.scale,
                                     self.ref_rect.h * self.scale)

    def strafe(self, dist):
        """ movement side to side 
        
        :param dist: takes in the distance moved positive left negative right
        """
        self.rect.x += dist * self.scale
        self.ref_rect.x += dist

    def walk(self, dist):
        """ forward and backwards movement of the player
        
        :param dist: distance moved positive away from player, negative towards
        """
        self.dist_to_plr += dist
        if self.dist_to_plr != 0:
            self.update_scale()

    def draw(self, surface:pygame.surface.Surface):
        """ displays or just blits to a surface which is passed
        
        :param surface(pygame.surface.Surface): surface on which to display the entity
        """
        if self.dist_to_plr > 0:
            pygame.draw.rect(surface,"black",(self.rect.x + c.WIDTH//2, self.rect.y, self.rect.w, self.rect.h))

    def tick(self):
        """
        per tick of the game this activates to allow animations and independent entity decisions
        
        """
        pass

    def update(self, *args, **kwargs):
        """ called by all entities at once, used for anything which needs to happen everywhere at once
        
        :param args: a series of inputs starting with a string to designate which function to use
                        then followed by any parameters needed for that function
        :param kwargs: as of yet unused, allows access to data which is not ordered through the use of a dictionary
        """
        if args[0] == "walk":
            self.walk(args[1])
        elif args[0] == "strafe":
            self.strafe(args[1])
        elif args[0] == "draw":
            self.draw(args[1])
        elif args[0] == "tick":
            self.tick()
        

