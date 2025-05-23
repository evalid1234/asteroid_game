import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *
from shot import * 

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!!")
    
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0
    
    Shot.containers = (shots_group, updateable_group, drawable_group)
    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    asteroid_field = AsteroidField()
    
    print(updateable_group, drawable_group, asteroids_group)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable_group.update(dt)
        for asteroid in asteroids_group:
            if asteroid.has_collided(player):
                print("Game over!")
                return 
            for bullet in shots_group:
                if asteroid.has_collided(bullet):
                    bullet.kill()
                    asteroid.split()
                    break
        for drawable_object in drawable_group:
            drawable_object.draw(screen)
        pygame.display.flip()
        dt = ( clock.tick(60) / 1000 )

     

if __name__ == "__main__":
   main()
