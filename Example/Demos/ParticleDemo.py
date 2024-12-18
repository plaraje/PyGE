import random
import pygame
from Objects import Scene
from Objects.Particles import Particle, ParticleProperties, ParticleSystem
from typing import List

class ParticleDemo(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.particle_systems: List[Particle] = []
        self.setup_particle_systems()

    def setup_particle_systems(self) -> None:
        # Sistema de partículas para el cursor
        self.cursor_particles = Particle(
            #max_particles=100,
            #spawn_rate=50,
           properties=ParticleProperties(
                position=pygame.mouse.get_pos(),
                velocity=(
                    random.uniform(-50, 50),
                    random.uniform(-50, 50)
                ),
                acceleration=(0, 98),
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                ),
                size=random.uniform(2, 5),
                lifetime=random.uniform(1, 2.5)
            )
        )
        #self.particle_systems.append(p for p in self.cursor_particles)
        for i in range(1,100):
            particle = Particle(
                #max_particles=100,
                #spawn_rate=50,
                properties=ParticleProperties(
                    position=pygame.mouse.get_pos(),
                    velocity=(
                        random.uniform(-50, 50),
                        random.uniform(-50, 50)
                    ),
                    acceleration=(0, 98),
                    color=(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    ),
                    size=random.uniform(2, 5),
                    lifetime=random.uniform(1, 2.5)
                )
            )
            self.particle_systems.append(particle)

    def update(self, delta_time: float) -> None:
        for i, system in enumerate(self.particle_systems):
            system.update(delta_time)
            if system.dead == True:
                self.particle_systems.pop(i)
        self.particle_systems.append(Particle(
                #max_particles=100,
                #spawn_rate=50,
                properties=ParticleProperties(
                    position=pygame.mouse.get_pos(),
                    velocity=(
                        random.uniform(-50, 50),
                        random.uniform(-50, 50)
                    ),
                    acceleration=(0, 98),
                    color=(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    ),
                    size=random.uniform(2, 5),
                    lifetime=random.uniform(1, 2.5)
                )
            ))

    def render(self, render_context) -> None:
        render_context.clear()
        for system in self.particle_systems:
            system.render(render_context)
