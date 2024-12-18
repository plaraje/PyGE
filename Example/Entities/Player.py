from Objects.Entities.Entity import Entity
from Objects.Colliders.AABBCollider import AABBCollider
from Objects.Physics.StandardPhysics import StandardPhysics
from Objects.Controllers.EntityControllers.PlayerController import PlayerController

class Player(Entity):
    def __init__(self, x, y, width, height, scene=None, color=(0, 255, 0)):
        physics = StandardPhysics(gravity=98, friction=20)
        collider = AABBCollider(x, y, width, height)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.scene = scene
        self.game = scene.game if scene else None
        self.controller = PlayerController(self)
        self.color = color
        self.outline_color = (0, 0, 0)
        self.outline_offset = 0

    def render(self, ctx, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_rounded_rect(adjusted_x, adjusted_y, self.width, self.height, self.color, 8)
        
        if self.outline_color:
            ctx.draw_rounded_rect(
                adjusted_x-self.outline_offset, adjusted_y-self.outline_offset, 
                self.width+2*self.outline_offset, self.height+2*self.outline_offset, 
                self.outline_color, 8,
                filled=False
            )

    def update(self, delta_time):
        self.controller.handle_input(delta_time)
        super().update(delta_time)
        print(f"Player position: ({self.x}, {self.y})")
        print(F"Player velocity: ({self.physics.vx}, {self.physics.vy})")

    def on_collision(self, platform):
        # Lógica para manejar la colisión con la plataforma
        self.physics.vy = 0  # Detener la caída
        self.y = platform.y - self.height  # Colocar al jugador encima de la plataforma



"""

from Objects.Entities.Entity import Entity
from Objects.Colliders.AABBCollider import AABBCollider
from Objects.Physics.StandardPhysics import StandardPhysics
from Objects.Controllers.EntityControllers.PlayerController import PlayerController

class Player(Entity):
    def __init__(self, x, y, width, height, scene=None, color = (0, 255, 0)):
        physics = StandardPhysics(gravity=980, friction=0)
        collider = AABBCollider(x, y, width, height)
        super().__init__(x, y, width, height, physics=physics, collider=collider)
        self.scene = scene
        self.game = scene.game if scene else None
        self.controller = PlayerController(self)
        self.color = color
        self.outline_color = None

    def render(self, ctx, camera_offset=(0, 0)):
        adjusted_x = self.x - camera_offset[0]
        adjusted_y = self.y - camera_offset[1]
        ctx.draw_rect(adjusted_x, adjusted_y, self.width, self.height, self.color)ç

        if self.outline_color:
            ctx.draw_rect(
                adjusted_x-2, adjusted_y-2, 
                self.width+4, self.height+4, 
                self.outline_color,
                filled=False
            )

    def update(self, delta_time):
        self.controller.handle_input(delta_time)
        super().update(delta_time)


"""