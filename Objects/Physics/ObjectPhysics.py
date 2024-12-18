class ObjectPhysics:
    def __init__(self, gravity=0, friction=0):
        self.gravity = gravity  # Aceleración en Y (e.g., caída libre)
        self.friction = friction  # Reducción de velocidad en X
        self.vx = 0  # Velocidad en X
        self.vy = 0  # Velocidad en Y
        print(f"Inited with: Gravity: {self.gravity}, Friction: {self.friction}")

    def apply_physics(self, entity, delta_time):
        """
        Aplica las reglas físicas al objeto (por defecto: gravedad y fricción).
        Este método puede ser sobrescrito en subclases.
        """
        # Gravedad (afecta la velocidad en Y)
        self.vy += self.gravity * delta_time


        # Fricción (reduce la velocidad en X)
        if self.friction > 0:
            if self.vx > 0:
                self.vx = max(0, self.vx - self.friction * delta_time)
            elif self.vx < 0:
                self.vx = min(0, self.vx + self.friction * delta_time)


        # Aplicar velocidades a la posición del Entity
        entity.x += self.vx * delta_time
        entity.y += self.vy * delta_time


    def on_collision(self, entity, collision_data):

        pass
