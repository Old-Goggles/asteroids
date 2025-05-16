import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.bumps = []
        num_vertices = random.randint(8, 12)
        for i in range(num_vertices):
            angle = 2 * math.pi * i / num_vertices
            bump_factor = random.uniform(0.7, 1.3)
            self.bumps.append((angle, bump_factor))
        
    def draw(self, screen):
        points = []
        for angle, bump_factor in self.bumps:
            bumpy_radius = self.radius * bump_factor
            x = self.position.x + math.cos(angle) * bumpy_radius
            y = self.position.y + math.sin(angle) * bumpy_radius
            points.append((int(x), int(y)))
        pygame.draw.polygon(screen, (0, 71, 171), points, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_position()
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2
