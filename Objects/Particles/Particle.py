from dataclasses import dataclass
import pygame
from typing import Tuple

@dataclass
class ParticleProperties:
    position: Tuple[float, float]
    velocity: Tuple[float, float]
    acceleration: Tuple[float, float] = (0, 0)
    color: Tuple[int, int, int] = (255, 255, 255)
    size: float = 5.0
    lifetime: float = 1.0
    alpha: int = 255

class Particle:
    def __init__(self, properties: ParticleProperties):
        self.x, self.y = properties.position
        self.vx, self.vy = properties.velocity
        self.ax, self.ay = properties.acceleration
        self.color = properties.color
        self.size = properties.size
        self.max_lifetime = properties.lifetime
        self.lifetime = properties.lifetime
        self.alpha = properties.alpha
        self.dead = False

    def update(self, delta_time: float) -> None:
        self.lifetime -= delta_time
        if self.lifetime <= 0:
            self.dead = True
            return

        # Actualizar velocidad
        self.vx += self.ax * delta_time
        self.vy += self.ay * delta_time

        # Actualizar posición
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

        # Actualizar alpha
        self.alpha = int((self.lifetime / self.max_lifetime) * 255)

    def render(self, render_context, camera_offset=(0, 0)) -> None:
        screen_x = self.x - camera_offset[0]
        screen_y = self.y - camera_offset[1]
        
        color_with_alpha = (*self.color, self.alpha)
        render_context.draw_circle(
            screen_x, screen_y, 
            self.size, 
            color_with_alpha
        )