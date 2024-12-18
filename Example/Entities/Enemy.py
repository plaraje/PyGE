from Objects.Entities import Entity
from Objects.Colliders.CircleCollider import CircleCollider
from Objects.Physics.BouncyPhysics import BouncyPhysics

class Enemy(Entity):
    def __init__(self, x, y, width, height):
        physics = BouncyPhysics(gravity=980, friction=0, bounce=0.8)
        collider = CircleCollider(x + width / 2, y + height / 2, width / 2)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.color = (255, 0, 0)

    def render(self, ctx, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_circle(
            adjusted_x + self.width / 2,
            adjusted_y + self.height / 2,
            self.width / 2,
            self.color
        )
