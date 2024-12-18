from dataclasses import dataclass
from typing import Optional
import pygame
from Objects.Core.RenderContext import RenderContext
from Objects.Core.Scene import Scene
from Objects.UI.UIManager import UIManager
from Objects.Input.KeyboardManager import KeyboardManager
from Objects.Input.MouseManager import MouseManager

@dataclass
class GameConfig:
    window_width: int = 800
    window_height: int = 600
    title: str = "Game Engine"
    target_fps: int = 60

class Game:
    def __init__(self, config: GameConfig = GameConfig()):
        pygame.init()
        
        # Configuración
        self.config: GameConfig = config
        self.screen: pygame.Surface = pygame.display.set_mode(
            (config.window_width, config.window_height)
        )
        pygame.display.set_caption(config.title)

        # Managers
        self.render_context: RenderContext = RenderContext(self.screen)
        self.ui_manager: UIManager = UIManager()
        self.keyboard_manager: KeyboardManager = KeyboardManager()
        self.mouse_manager: MouseManager = MouseManager()
        
        # Control de tiempo
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.paused: bool = False
        self.fixed_time_step: float = 1/config.target_fps
        self.accumulated_time: float = 0

        # Escena
        self.current_scene: Optional[Scene] = None

    def set_scene(self, scene: Scene) -> None:
        self.current_scene = scene

    def quit(self):
        """Método para cerrar el juego"""
        self.running = False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.WINDOWFOCUSLOST:
                self.paused = True
            elif event.type == pygame.WINDOWFOCUSGAINED:
                self.paused = False
            
            self.keyboard_manager.handle_event(event)
            self.mouse_manager.handle_event(event)
            self.ui_manager.handle_event(event)
            self.current_scene.handle_event(event)

    def update(self, delta_time):
        if self.paused:
            return

        self.accumulated_time += delta_time
        
        while self.accumulated_time >= self.fixed_time_step:
            self.fixed_update(self.fixed_time_step)
            self.accumulated_time -= self.fixed_time_step
        
        self.keyboard_manager.update(delta_time)
        self.mouse_manager.update(delta_time)
        self.current_scene.update(delta_time)
        self.ui_manager.update(delta_time)

    def fixed_update(self, fixed_delta):
        self.current_scene.fixed_update(fixed_delta)

    def render(self):
        self.render_context.clear()
        self.current_scene.render(self.render_context)
        self.ui_manager.render(self.render_context)
        self.render_context.flip()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0
            self.handle_input()
            self.update(delta_time)
            self.render()

        pygame.quit()