from Objects.Core import RenderContext
from Objects.Entities import Entity
from Objects.Colliders.CircleCollider import CircleCollider
from Objects.Physics.NoGravityPhysics import NoGravityPhysics
from Example.Behaviours.TestBehaviour import TestBehaviour

class Enemy(Entity):
    def __init__(self, x, y, width, height):
        physics = NoGravityPhysics(friction=800, max= 100)
        collider = CircleCollider(x + width / 2, y + height / 2, width / 2)
        self.behaviour = TestBehaviour(self)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.color = (255, 0, 0)

    def update(self, delta_time):
        super().update(delta_time)
        self.behaviour.update(delta_time)

    def render(self, ctx: RenderContext, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_circle(
            adjusted_x + self.width / 2,
            adjusted_y + self.height / 2,
            self.width / 2,
            self.color
        )
        ctx.draw_text(
            str(f"VX: {self.physics.vx}"),
            adjusted_x + self.width / 2,
            adjusted_y + self.height / 2,
            color=(0, 50, 0),
            size=15
        )

        ctx.draw_text(
            str(f"VY: {self.physics.vy}"),
            adjusted_x + self.width / 2,
            (adjusted_y + self.height / 2) + 15,
            color=(0, 50, 0),
            size=15
        )
