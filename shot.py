from constants import SHOT_RADIUS
from circleshape import * 

class Shot(CircleShape):
    def __init__(self, x,  y):
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
    def update(self, dt):
        self.position += dt * self.velocity

