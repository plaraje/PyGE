from typing import List, Tuple
import pygame
from Objects import Scene, Camera
from Objects.UI import Button, Panel, UIManager, Label
from Example.Entities.Player import Player
from Example.Entities.Platform import Platform
from Objects.Core import Game
from Objects.Core.RenderContext import RenderContext
from Objects.Debug import DebugInfo
from Objects.Particles import ParticleSystem, ParticleProperties
import random

class GameScene(Scene):
    def __init__(self, game: 'Game') -> None:
        super().__init__(game)
        self.setup_world()
        self.setup_entities()
        self.setup_camera()
        self.setup_ui()
        self.particle_system = ParticleSystem(
            max_particles=100,
            spawn_rate=50,
            particle_properties=lambda: ParticleProperties(
                position=(self.player.x + (self.player.width/2), self.player.y + (self.player.height * 0.75)),
                velocity=(random.uniform(-50, 50), random.uniform(-50, 50)),
                acceleration=(0, 98),
                color=(random.uniform(100, 255), 255, 0),
                size=random.uniform(1, 3),
                lifetime=random.uniform(1, 3)
            )
        )

    def setup_world(self) -> None:
        self.world_bounds: Tuple[int, int, int, int] = (0, 0, 2000, 1500)

    def setup_camera(self) -> None:
        self.camera = Camera(
            self.game.config.window_width,
            self.game.config.window_height,
            world_bounds=self.world_bounds
        )
        self.camera.follow(self.player, deadzone=(50, 50))

    def setup_entities(self) -> None:
        self.player = Player(100, 100, 50, 50, scene=self)
        self.setup_platforms()

    def setup_platforms(self) -> None:
        self.platforms: List[Platform] = [
            Platform(0, 1200, 2000, 50),  # Suelo
            Platform(300, 800, 200, 20),
            Platform(600, 700, 200, 20),
            Platform(100, 600, 200, 20),
            Platform(800, 750, 200, 20),
        ]
        
        # Añadir bordes del mundo
        self.platforms.extend([
            Platform(-50, 0, 50, self.world_bounds[3]),     # Izquierdo
            Platform(self.world_bounds[2], 0, 50, self.world_bounds[3]),  # Derecho
            Platform(0, -50, self.world_bounds[2], 50),     # Techo
        ])

    def setup_ui(self) -> None:
        self.paused = False
        self.setup_pause_menu()
        self.setup_debug_info()

    def setup_pause_menu(self) -> None:
        self.pause_panel = Panel(
            self.game.config.window_width/2 - 150,
            self.game.config.window_height/2 - 200,
            300, 400,
            color=(40, 40, 40, 200)
        )
        
        text_label = Label(50, 30, 200, 50, "PAUSED", text_color=(255, 255, 255), font_size=44)

        resume_btn = Button(50, 100, 200, 50, "Resume", self.toggle_pause,
                            normal_color=(100, 100, 150), hover_color=(120, 120, 170), pressed_color=(80, 80, 130)
                    )
        restart_btn = Button(50, 170, 200, 50, "Restart", self.restart_game)
        quit_btn = Button(50, 240, 200, 50, "Quit", self.game.quit, 
                          normal_color=(150, 100, 100), hover_color=(170, 120, 120), pressed_color=(130, 80, 80)
                    )
        debug_btn = Button(
            50, 310, 200, 50,
            "Debug Info",
            lambda: setattr(self.debug_info, 'visible', not self.debug_info.visible),
            normal_color=(50, 50, 50), hover_color=(70, 70, 70), pressed_color=(30, 30, 30)
        )
        
        self.pause_panel.add_child(text_label)
        self.pause_panel.add_child(resume_btn)
        self.pause_panel.add_child(restart_btn)
        self.pause_panel.add_child(quit_btn)
        self.pause_panel.add_child(debug_btn)
        self.pause_panel.visible = False

    def setup_debug_info(self) -> None:
        self.debug_info = DebugInfo()
        
        # Añadir valores a monitorear
        self.debug_info.add_value("FPS", lambda: int(self.game.clock.get_fps()))
        self.debug_info.add_value("X", lambda: round(self.player.x, 2))
        self.debug_info.add_value("Y", lambda: round(self.player.y, 2))
        self.debug_info.add_value("VX", lambda: round(self.player.physics.vx, 2))
        self.debug_info.add_value("VY", lambda: round(self.player.physics.vy, 2))
        self.debug_info.add_value("IS_GROUNDED", lambda: self.player.physics.is_grounded)
        

    def toggle_pause(self) -> None:
        self.paused = not self.paused
        self.pause_panel.visible = self.paused

    def restart_game(self) -> None:
        self.player.x = 100
        self.player.y = 100
        self.player.physics.vx = 0
        self.player.physics.vy = 0
        self.toggle_pause()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.toggle_pause()
        
        if self.paused:
            self.pause_panel.handle_event(event)

    def update(self, delta_time: float) -> None:
        if not self.paused:
            self.camera.update(delta_time)
            self.particle_system.update(delta_time)

    def fixed_update(self, fixed_delta: float) -> None:
        if not self.paused:
            self.player.update(fixed_delta)
            
            for platform in self.platforms:
                if self.player.collides_with(platform):
                    self.player.physics.on_collision(self.player, platform)

    def render(self, render_context: 'RenderContext') -> None:
        render_context.clear()

        self.mountain_offset = self.camera.viewport.x * 0.2
        
        # Dibujar montañas en diferentes capas
        render_context.draw_mountains(
            base_y=render_context.height - 100,
            color=(60, 63, 65),
            offset_x=self.mountain_offset * 0.3,
            height_factor=1.2
        )
        render_context.draw_mountains(
            base_y=render_context.height - 50,
            color=(51, 53, 56),
            offset_x=self.mountain_offset * 0.6,
            height_factor=0.8
        )
        render_context.draw_mountains(
            base_y=render_context.height,
            color=(40, 42, 45),
            offset_x=self.mountain_offset,
            height_factor=0.5
        )

        for platform in self.platforms:
            platform.render(render_context, camera_offset=(self.camera.viewport.x, self.camera.viewport.y))
        self.particle_system.render(render_context, camera_offset=(self.camera.viewport.x, self.camera.viewport.y))
        self.player.render(render_context, camera_offset=(self.camera.viewport.x, self.camera.viewport.y))
        
        # UI
        self.debug_info.render(render_context)

        # Pausa panel
        if self.paused:
            self.pause_panel.render(render_context)