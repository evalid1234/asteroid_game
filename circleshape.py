import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass
    def has_collided(self, other_circle):
        min_collision_dist = self.radius + other_circle.radius
        if self.position.distance_to(other_circle.position) <= min_collision_dist:
            return True
        return False

    def update(self, dt):
        # sub-classes must override
        pass
