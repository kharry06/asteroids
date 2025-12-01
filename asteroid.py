from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")
            ang = random.uniform(20, 50)
            vel1 = self.velocity.rotate(ang)
            vel2 = self.velocity.rotate(-ang)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast2 = Asteroid(self.position.x, self.position.y, new_rad)
            ast1.velocity = vel1
            ast2.velocity = vel2

            self.kill()
