import pygame # type: ignore
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid split")
            ang = random.uniform(20, 50)
            vec1 = self.velocity.rotate(ang)
            vec2 = self.velocity.rotate(-ang)
            newRad = self.radius - ASTEROID_MIN_RADIUS
            newA = Asteroid(self.position.x, self.position.y, newRad)
            newB = Asteroid(self.position.x, self.position.y, newRad)
            newA.velocity = vec1 * 1.2
            newB.velocity = vec2 * 1.2


