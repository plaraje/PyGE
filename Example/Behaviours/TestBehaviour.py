import math
from Objects.Entities.Entity import Entity


class TestBehaviour:
    def __init__(self, entity):
        self.entity: 'Entity' = entity
        self.enabled = True
        self.objetive: 'Entity' | None = None
        self.min_distance = 5  # Distancia mínima para considerar que llegó al objetivo
        self.max_speed = 150  # Velocidad máxima

    def on_attach(self, entity):
        self.entity = entity

    def on_detach(self):
        self.entity = None

    def set_objetive(self, objetive):
        self.objetive = objetive

    def get_objetive(self):
        return self.objetive

    def update(self, delta_time):
        if not self.enabled:
            return

        physics = self.entity.physics
        objetive = self.objetive

        if not physics:
            print("No physics component found")
            return

        if not objetive:
            print("No objective found")
            # Aplicar fricción para detener movimiento en ambos ejes
            physics.vx *= 0.98  # Fricción en el eje X
            physics.vy *= 0.98  # Fricción en el eje Y
            return

        # Calcular dirección hacia el objetivo
        dx = objetive.x - self.entity.x
        dy = objetive.y - self.entity.y
        distance = math.sqrt(dx ** 2 + dy ** 2) * 0.01

        # Si el objetivo se está moviendo, predecir su posición futura
        if hasattr(objetive, 'vx') and hasattr(objetive, 'vy'):
            future_x = objetive.x + objetive.vx * delta_time
            future_y = objetive.y + objetive.vy * delta_time
            dx = future_x - self.entity.x
            dy = future_y - self.entity.y

        # Normalizar dirección
        if distance > 0:
            direction_x = dx / distance
            direction_y = dy / distance
        else:
            direction_x = 0
            direction_y = 0

        # Aplicar velocidad hacia el objetivo con el comportamiento de 'arrive'
        arrival_distance = self.min_distance
        if distance < arrival_distance:
            # Si está cerca del objetivo, disminuir la velocidad
            speed = self.max_speed * (distance / arrival_distance)
        else:
            # Si está lejos, mantener velocidad máxima
            speed = self.max_speed

        # Actualizar velocidad con la dirección normalizada
        physics.vx += direction_x * speed * delta_time
        physics.vy += direction_y * speed * delta_time

        # Aplicar límites de velocidad y fricción
        physics.vx = min(max(-self.max_speed, physics.vx), self.max_speed)
        physics.vy = min(max(-self.max_speed, physics.vy), self.max_speed)

        # Aplicar fricción adicional si no se está moviendo hacia un objetivo
        if not objetive:
            physics.vx *= 0.98
            physics.vy *= 0.98
