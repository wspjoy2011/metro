from random import random

from solar_system_new.classes.planet_data import PlanetData
from solar_system_new.classes.planet import Planet


class Asteroid(Planet):
    start_angle = 0.001
    increase_start_angle = 0.012421

    def __init__(self, star, radius):
        self.obj = PlanetData((0.1, 0.1), self.generate_color(), radius, self.increase_start_angle)
        Planet.__init__(self, self.obj, star)
        self.angle += self.start_angle
        Asteroid.start_angle += self.increase_start_angle

    @staticmethod
    def generate_color():
        return random(), random(), random()
