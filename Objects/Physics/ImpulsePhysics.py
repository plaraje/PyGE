from .ObjectPhysics import ObjectPhysics

class ImpulsePhysics(ObjectPhysics):
    def __init__(self, gravity=9.8):
        super().__init__(gravity)
        self.impulses = []

    def apply_physics(self, entity, delta_time):
        super().apply_physics(entity, delta_time)
        
        for fx, fy in self.impulses:
            self.vx += fx * delta_time
            self.vy += fy * delta_time
        self.impulses.clear()

    def add_impulse(self, fx, fy):
        self.impulses.append((fx, fy))
