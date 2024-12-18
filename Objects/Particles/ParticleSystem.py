import random
import pygame
from .Particle import Particle, ParticleProperties

class ParticleSystem:
    def __init__(self, max_particles, spawn_rate, particle_properties):
        self.max_particles = max_particles
        self.spawn_rate = spawn_rate
        self.particle_properties = particle_properties
        self.particles = []
        self.time_since_last_spawn = 0

    def update(self, delta_time):
        self.time_since_last_spawn += delta_time

        # Generar nuevas partículas
        while self.time_since_last_spawn >= 1 / self.spawn_rate:
            if len(self.particles) < self.max_particles:
                properties = self.particle_properties()
                self.particles.append(Particle(properties))
            self.time_since_last_spawn -= 1 / self.spawn_rate

        # Actualizar partículas existentes
        for particle in self.particles[:]:
            particle.update(delta_time)
            if particle.dead:
                self.particles.remove(particle)

    def render(self, render_context, camera_offset=(0, 0)):
        for particle in self.particles:
            particle.render(render_context, camera_offset)