import pygame
import world

jumping_force = 10

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.vel_y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.jumped = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def apply_gravity(self):
        gravity = 1

        self.vel_y += gravity
        
        max_fall_speed = 10
        if self.vel_y > max_fall_speed:
            self.vel_y = max_fall_speed

        self.y += self.vel_y

        if self.y < 0:
            self.y = 0

        elif self.y > world.height - self.height:
            self.y = world.height - self.height
        
        self.rect.y = self.y

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not self.jumped:
                self.vel_y = -jumping_force
                self.jumped = True

        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.y += self.vel




        #gravity
        # self.vel_y += 0.6 #gravity force
        # self.y += self.vel_y

        #self.update()

        #collision:

        for tile in world.world.tile_list:
            tile_rect = tile[1]  # Get the rect from the tile tuple

            # Check for collision in X
            if tile_rect.colliderect(self.rect.x + self.x, self.rect.y, self.width, self.height):
                self.x = 0

            # Check for collision in Y
            if tile_rect.colliderect(self.rect.x, self.rect.y + self.y, self.width, self.height):
                # Check if below the ground (e.g., jumping)
                if self.vel_y < 0:
                    self.y = tile_rect.bottom - self.rect.top
            # Check if above the ground (e.g., falling)
            if self.vel_y >= 0:
                self.y = tile_rect.top - self.rect.bottom
                self.jumped = False

      

        self.rect.x += self.x
        self.rect.y += self.y

        
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)