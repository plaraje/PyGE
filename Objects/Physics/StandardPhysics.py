import pygame
from .ObjectPhysics import ObjectPhysics
import copy

class StandardPhysics(ObjectPhysics):
    def __init__(self, gravity=9.8, friction=0.2, bounce=0.5, gravity_modifier=1.0):
        super().__init__(gravity=gravity, friction=friction)
        self.bounce = bounce
        self.is_grounded = False
        self.last_position = None
        self.gavity_modifier = gravity_modifier
        self.ground_check_distance = 2

    def apply_physics(self, entity, delta_time):
        super().apply_physics(entity, delta_time)
        self.last_position = (entity.x, entity.y)
        self.is_grounded = False
        
        # Aplicar gravedad
        self.vy += self.gravity * delta_time

        # Limitar velocidades máximas
        max_speed = 1000
        self.vx = max(min(self.vx, max_speed), -max_speed)
        self.vy = max(min(self.vy, max_speed), -max_speed)

        # Aplicar velocidades
        entity.x += self.vx * delta_time
        entity.y += self.vy * delta_time

        if self.vy == 0:
            self.is_grounded = True
            
        self.check_grounded(entity)
        
        # Actualizar collider
        entity.update_collider()

    def on_collision(self, entity, other):
        if not self.last_position:
            return

        # Lógica para determinar si el jugador está en el suelo
        if other.y > entity.y + entity.height:  # Si colisiona desde arriba
            self.is_grounded = True
            entity.y = other.y - entity.height  # Coloca al jugador encima de la plataforma
        else:
            self.is_grounded = False  # Si no está en el suelo, no está "grounded"

        # Restaurar posición anterior
        prev_x, prev_y = self.last_position
        
        # Detectar dirección de colisión usando el centro de las entidades
        entity_center = (entity.x + entity.width/2, entity.y + entity.height/2)
        other_center = (other.x + other.width/2, other.y + other.height/2)
        
        dx = entity_center[0] - other_center[0]
        dy = entity_center[1] - other_center[1]

        # Calcular las proporciones de penetración
        overlap_x = (abs(dx) - (entity.width + other.width) / 2)
        overlap_y = (abs(dy) - (entity.height + other.height) / 2)

        # Resolver colisión basado en la dirección más cercana
        if abs(overlap_x) < abs(overlap_y):
            # Colisión horizontal
            if dx > 0:
                entity.x = other.x + other.width
                self.vx = -self.vx * self.bounce  # Aplicar rebote
            else:
                entity.x = other.x - entity.width
                self.vx = -self.vx * self.bounce  # Aplicar rebote
        else:
            # Colisión vertical
            if dy > 0:
                entity.y = other.y + other.height
                self.vy = 0
            else:
                entity.y = other.y - entity.height
                self.vy = 0
                self.is_grounded = True

        entity.update_collider()

    def check_grounded(self, entity):
        # Crear un rectángulo justo debajo del entity para verificar colisiones con el suelo

        ground_check_bottom = entity.y + entity.height + self.ground_check_distance

        # Verificar colisiones con todas las plataformas
        for platform in entity.scene.platforms:
            if (entity.x < platform.x + platform.width and
                entity.x + entity.width > platform.x and
                ground_check_bottom >= platform.y and
                entity.y + entity.height <= platform.y):
                self.is_grounded = True
                return

        self.is_grounded = False

    def copy(self):
        return copy.deepcopy(self)

