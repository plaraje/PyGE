from Objects.Core.RenderContext import RenderContext
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
        self.previous_physics = physics

    def render(self, ctx: RenderContext, camera_offset=(0, 0)):
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
        
        ctx.draw_circle(adjusted_x + self.width * 0.3, adjusted_y + self.height * 0.3, 8, (255, 255, 255))
        ctx.draw_circle(adjusted_x + self.width * 0.7, adjusted_y + self.height * 0.3, 8, (255, 255, 255))
        if self.physics.vx > 10:
            ctx.draw_circle(adjusted_x + 3 + self.width * 0.3, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
            ctx.draw_circle(adjusted_x + 3 + self.width * 0.7, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
        elif self.physics.vx < -10:
            ctx.draw_circle(adjusted_x - 3 + self.width * 0.3, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
            ctx.draw_circle(adjusted_x - 3 + self.width * 0.7, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
        else:
            ctx.draw_circle(adjusted_x + self.width * 0.3, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
            ctx.draw_circle(adjusted_x + self.width * 0.7, adjusted_y + self.height * 0.3, 3, (0, 0, 0))
        
        if self.physics.is_grounded:
            ctx.draw_line((adjusted_x + self.width * 0.3, adjusted_y + self.height * 0.8),
                          (adjusted_x + self.width * 0.7, adjusted_y + self.height * 0.8),
                          (255, 0, 0), 3)
        else:
            ctx.draw_circle(adjusted_x + self.width * 0.5, adjusted_y + self.height * 0.8, 5, (255, 0, 0))
            ctx.draw_circle(adjusted_x + self.width * 0.5, adjusted_y + self.height * 0.8, 2, (0, 255, 0))

    def update(self, delta_time):
        self.previous_physics = self.physics.copy()
        self.controller.handle_input(delta_time)
        super().update(delta_time)
        print(f"Player position: ({self.x}, {self.y})")
        print(F"Player velocity: ({self.physics.vx}, {self.physics.vy})")

    def on_collision(self, platform):
        # Lógica para manejar la colisión con la plataforma
        self.physics.vy = 0  # Detener la caída
        self.y = platform.y - self.height  # Colocar al jugador encima de la plataforma


