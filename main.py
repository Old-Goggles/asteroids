import pygame
import sys
import os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ui import display_score

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_path = os.path.join(current_dir, "background.jpg")

    try:
        background = pygame.image.load(background_path).convert()
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except pygame.error as e:
        print(f"Error loading background: {e}")
        wbackground = None

    score = 0
    consecutive_hits = 0
    multiplier = 1

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)

    dt = 0

    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            if player_instance.collision(asteroid):
                print("Game over!")
                sys.exit()    

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    consecutive_hits += 1
                    multiplier = 1 + (consecutive_hits // 10)
                    if asteroid.radius >= 40:  
                        score += 10 * multiplier
                    elif asteroid.radius >= 20:  
                        score += 5 * multiplier
                    else:  
                        score += 1 * multiplier
                    shot.kill()
                    asteroid.split()

        for shot in shots.copy():
            if (shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or 
                shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT):
                shot.kill()
                consecutive_hits = 0
                multiplier = 1

        screen.fill((0, 0, 0))

        if background:
            screen.blit(background, (0, 0))

        for sprite in drawable:
            sprite.draw(screen) 

        display_score(screen, score, multiplier, consecutive_hits)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
