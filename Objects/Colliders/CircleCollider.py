import math
from . import Collider

class CircleCollider(Collider):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def collides_with(self, other):
        if isinstance(other, CircleCollider):
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return distance <= (self.radius + other.radius)
        return False
