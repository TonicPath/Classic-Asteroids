import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS




class Asteroid(CircleShape):
    def __init__(self,x: float, y: float, radius: float)-> None:
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_number = random.uniform(20,50)
            first_asteroid_split_vector = self.velocity.rotate(random_number)
            second_asteroid_split_vector = self.velocity.rotate(-random_number)
            split_asteroids_new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, split_asteroids_new_radius)
            asteroid_1.velocity = first_asteroid_split_vector * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, split_asteroids_new_radius)
            asteroid_2.velocity = second_asteroid_split_vector * 1.2


