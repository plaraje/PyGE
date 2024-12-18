from .Entity import Entity
from ..Colliders.AABBCollider import AABBCollider
from ..Physics.StandardPhysics import StandardPhysics
from ..Controllers.EntityControllers.PlayerController import PlayerController

class Player(Entity):
    def __init__(self, x, y, width, height, scene=None):
        physics = StandardPhysics(gravity=980, friction=0)
        collider = AABBCollider(x, y, width, height)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.scene = scene
        self.game = scene.game if scene else None
        self.controller = PlayerController(self)

    def render(self, ctx, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_rect(adjusted_x, adjusted_y, self.width, self.height, (0, 255, 0))

    def update(self, delta_time):
        self.controller.handle_input(delta_time)
        super().update(delta_time)

