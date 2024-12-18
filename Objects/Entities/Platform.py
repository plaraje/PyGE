from .Entity import Entity
from ..Colliders.AABBCollider import AABBCollider
from ..Physics.NoGravityPhysics import NoGravityPhysics

class Platform(Entity):
    def __init__(self, x, y, width, height):
        physics = NoGravityPhysics()  # Las plataformas no se mueven
        collider = AABBCollider(x, y, width, height)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.z_index = -1  # Para que se renderice detrás de otros objetos

    def render(self, ctx, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_rect(adjusted_x, adjusted_y, self.width, self.height, (0, 100, 255))