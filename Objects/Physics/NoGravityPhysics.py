from .ObjectPhysics import ObjectPhysics

class NoGravityPhysics(ObjectPhysics):
    def __init__(self, friction=0.05):
        super().__init__(gravity=0, friction=friction)

    def on_collision(self, entity, collision_data):
        """
        Solo detiene al objeto en colisiones.
        """
        if collision_data["normal"] == "bottom":
            self.vy = 0
