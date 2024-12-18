from . import Collider

class AABBCollider(Collider):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def collides_with(self, other):
        if isinstance(other, AABBCollider):
            return (
                self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y
            )
        return False  # Maneja otros tipos de colisión aquí
