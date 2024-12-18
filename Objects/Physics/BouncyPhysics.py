from .StandardPhysics import StandardPhysics
import random

class BouncyPhysics(StandardPhysics):
    def __init__(self, gravity=980, friction=0, bounce=0.8):
        super().__init__(gravity, friction, bounce)
        self.vx = random.uniform(-200, 200)  # Velocidad inicial aleatoria
        self.vy = random.uniform(-200, 200)

    def on_collision(self, entity, other):
        if not self.last_position:
            return

        entity_center = (entity.x + entity.width/2, entity.y + entity.height/2)
        other_center = (other.x + other.width/2, other.y + other.height/2)
        
        dx = entity_center[0] - other_center[0]
        dy = entity_center[1] - other_center[1]

        if abs(dx/other.width) > abs(dy/other.height):
            # Colisión horizontal
            self.vx = -self.vx * self.bounce
            if dx > 0:
                entity.x = other.x + other.width
            else:
                entity.x = other.x - entity.width
        else:
            # Colisión vertical
            self.vy = -self.vy * self.bounce
            if dy > 0:
                entity.y = other.y + other.height
            else:
                entity.y = other.y - entity.height
                self.is_grounded = True

        # Añadir un poco de aleatoriedad en el rebote
        self.vx += random.uniform(-50, 50)
        self.vy += random.uniform(-50, 50)

        entity.update_collider()