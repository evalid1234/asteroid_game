from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    __AST_WIDTH = 2
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.__AST_WIDTH)
    def update(self, dt):
        self.position += dt * self.velocity
    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        angles = random.uniform(20,50)
        rotate_one =(self.velocity.rotate(angles))
        rotate_two =(self.velocity.rotate(-angles))
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        SPLIT_SPEED_UP = 1.2
        Asteroid(self.position[0], self.position[1], new_radius).velocity=rotate_one * SPLIT_SPEED_UP
        Asteroid(self.position[0], self.position[1], new_radius).velocity=rotate_two * SPLIT_SPEED_UP
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.__AST_WIDTH)
    def update(self, dt):
        self.position += dt * self.velocity
    

