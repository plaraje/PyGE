import random
import pygame
from Objects import Scene
from Objects.Cameras.Camera import Camera
from Objects.Core.Game import Game
from Objects.Core.RenderContext import RenderContext
from Objects.Particles.Particle import ParticleProperties
from Objects.Particles.ParticleSystem import ParticleSystem
from Objects.UI import Button, Label
from Objects.UI.Panel import Panel


class MainMenuScene(Scene):
    def __init__(self, game: 'Game') -> None:
        super().__init__(game)
        self.setup_camera()
        self.setup_ui()
        """self.particle_system = ParticleSystem(
            max_particles=100,
            spawn_rate=50,
            particle_properties=lambda: ParticleProperties(
                position=pygame.mouse.get_pos(),
                velocity=(random.uniform(-50, 50), random.uniform(-50, 50)),
                acceleration=(0, 98),
                color=(random.uniform(100, 255), 255, 0),
                size=random.uniform(1.0, 2.0),
                lifetime=random.uniform(1, 5)
            )
        )"""

    def setup_camera(self) -> None:
        self.camera = Camera(
            self.game.config.window_width,
            self.game.config.window_height,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        

        self.ui_panel.handle_event(event)
    
    def setup_ui(self) -> None:
        self.ui_panel = Panel(
            0, 0,
            self.game.config.window_width + 150,
            self.game.config.window_height + 150,
            color=(20, 20, 20, 255)
        )
        
        text_label = Label(self.game.config.window_width/2 - 100, 30, 200, 50, "GE TEST - Plaraje", text_color=(255, 255, 255), font_size=64)

        play_btn = Button(self.game.config.window_width/2 - 100, 100, 200, 50, 
                            "Play!",
                            self.start_game,
                            normal_color=(100, 100, 150), hover_color=(120, 120, 170), pressed_color=(80, 80, 130)
                    )
        
        quit_btn = Button(self.game.config.window_width/2 - 100, 240, 200, 50, "Quit", self.game.quit, 
                          normal_color=(150, 100, 100), hover_color=(170, 120, 120), pressed_color=(130, 80, 80)
                    )

        """
        restart_btn = Button(50, 170, 200, 50, "Restart", self.restart_game)
        
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
        self.pause_panel.add_child(debug_btn)"""
        self.ui_panel.add_child(text_label)
        self.ui_panel.add_child(play_btn)
        self.ui_panel.add_child(quit_btn)
        self.ui_panel.visible = True

    def start_game(self) -> None:
        from Example.Scenes.GameScene import GameScene
        self.game.set_scene(GameScene(self.game))
        print("Starting game...")

    def update(self, delta_time: float) -> None:
        self.camera.update(delta_time)
        #self.particle_system.update(delta_time)

    def fixed_update(self, fixed_delta: float) -> None:
        pass


    def render(self, render_context: RenderContext) -> None:
        self.ui_panel.render(render_context)
        #self.particle_system.render(render_context)


        