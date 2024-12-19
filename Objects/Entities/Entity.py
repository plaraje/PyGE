from Objects.Physics.ObjectPhysics import ObjectPhysics
from ..Colliders.AABBCollider import AABBCollider
from ..Colliders.CircleCollider import CircleCollider
from ..Core.Renderable import Renderable

class Entity(Renderable):
    def __init__(self, x=0, y=0, width=0, height=0, physics=None, collider=None):
        super().__init__(x, y, width, height)
        self.physics: 'ObjectPhysics' = physics
        self.collider = collider
        if self.collider:
            self.update_collider()

    def render(self, ctx, camera_offset=(0, 0)):
        pass

    def update_collider(self):
        if self.collider:
            if isinstance(self.collider, AABBCollider):
                self.collider.x = self.x
                self.collider.y = self.y
                self.collider.width = self.width
                self.collider.height = self.height
            elif isinstance(self.collider, CircleCollider):
                self.collider.x = self.x + self.width / 2
                self.collider.y = self.y + self.height / 2

    def update(self, delta_time):
        if self.physics:
            self.physics.apply_physics(self, delta_time)
        self.update_collider()

    def on_collision(self, collision_data):
        if self.physics:
            self.physics.on_collision(self, collision_data)
    
    def collides_with(self, other):
        if self.collider and other.collider:
            return self.collider.collides_with(other.collider)
        return False
