from .ObjectPhysics import ObjectPhysics

class NoGravityPhysics(ObjectPhysics):
    def __init__(self, friction=0.05, max: int | None = None):
        super().__init__(gravity=0, friction=friction)
        self.max = max 

    def on_collision(self, entity, collision_data):
        """
        Solo detiene al objeto en colisiones.
        """
        if collision_data["normal"] == "bottom":
            self.vy = 0

    def apply_physics(self, entity, delta_time):

        if self.friction > 0:
            if self.vx > 0:
                self.vx = max(0, self.vx - self.friction * delta_time)
            elif self.vx < 0:
                self.vx = min(0, self.vx + self.friction * delta_time)



        self.vx = max(0, self.vx) if self.max else self.vx
        self.vy = max(0, self.vy) if self.max else self.vy


        entity.x += self.vx * delta_time
        entity.y += self.vy * delta_time
