from ..Core.Viewport import Viewport
from ..Core.Renderable import Renderable
import random

class Camera:
    def __init__(self, width, height, world_bounds=None):
        self.viewport = Viewport(0, 0, width, height)
        self.world_bounds = world_bounds or (0, 0, width * 2, height * 2)
        self.target = None
        self.deadzone = (100, 100)
        self.shake_amount = 0
        self.shake_duration = 0
        self.zoom_level = 1.0
        self.target_zoom = 1.0
        self.zoom_speed = 2.0
        self.smooth_factor = 0.1
        self.base_zoom = 1.0

    def follow(self, target, deadzone=None):
        self.target = target
        if deadzone:
            self.deadzone = deadzone

    def shake(self, amount, duration):
        self.shake_amount = amount
        self.shake_duration = duration

    def set_zoom(self, level, immediate=False):
        self.target_zoom = max(0.5, min(2.0, level))
        if immediate:
            self.zoom_level = self.target_zoom
            self.viewport.zoom = self.zoom_level

    def update(self, delta_time):
        if not self.target:
            return

        # Actualizar zoom suavemente
        if self.zoom_level != self.target_zoom:
            zoom_diff = self.target_zoom - self.zoom_level
            self.zoom_level += zoom_diff * self.zoom_speed * delta_time
            self.viewport.zoom = self.zoom_level


        # Calcular el centro del objetivo
        target_center_x = self.target.x + self.target.width / 2
        target_center_y = self.target.y + self.target.height / 2

        # Calcular el tamaño de la ventana ajustado por el zoom
        viewport_width = self.viewport.width / self.zoom_level
        viewport_height = self.viewport.height / self.zoom_level

        # Calcular la posición deseada de la cámara
        desired_x = target_center_x - viewport_width / 2
        desired_y = target_center_y - viewport_height / 2

        # Aplicar deadzone
        current_x = self.viewport.x
        current_y = self.viewport.y
        
        dx = desired_x - current_x
        dy = desired_y - current_y

        if abs(dx) > self.deadzone[0]:
            if dx > 0:
                self.viewport.x += (dx - self.deadzone[0]) * self.smooth_factor
            else:
                self.viewport.x += (dx + self.deadzone[0]) * self.smooth_factor

        if abs(dy) > self.deadzone[1]:
            if dy > 0:
                self.viewport.y += (dy - self.deadzone[1]) * self.smooth_factor
            else:
                self.viewport.y += (dy + self.deadzone[1]) * self.smooth_factor

        # Actualizar shake
        if self.shake_duration > 0:
            self.viewport.x += random.uniform(-self.shake_amount, self.shake_amount)
            self.viewport.y += random.uniform(-self.shake_amount, self.shake_amount)
            self.shake_duration -= delta_time
            if self.shake_duration <= 0:
                self.shake_amount = 0

        # Aplicar límites del mundo
        self.viewport.x = max(self.world_bounds[0], 
                            min(self.viewport.x, 
                                self.world_bounds[2] - self.viewport.width))
        self.viewport.y = max(self.world_bounds[1], 
                            min(self.viewport.y, 
                                self.world_bounds[3] - self.viewport.height))

    def get_render_list(self, entities):
        visible_entities = []
        for entity in entities:
            if self.viewport.contains(entity):
                visible_entities.append(entity)
        return sorted(visible_entities, key=lambda e: e.z_index)

    def render(self, context, entities):
        render_list = self.get_render_list(entities)
        for entity in render_list:
            rel_x, rel_y = self.viewport.get_relative_position(entity.x, entity.y)
            entity.render(context, camera_offset=(self.viewport.x, self.viewport.y))
