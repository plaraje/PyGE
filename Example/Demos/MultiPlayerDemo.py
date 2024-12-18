import pygame
from typing import List, Optional
from Objects import Scene, Camera
from Example.Entities.Player import Player
from Example.Entities.Platform import Platform

class MultiPlayerDemo(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.setup_world()
        self.setup_players()
        self.setup_camera()

    def setup_world(self) -> None:
        self.world_bounds = (0, 0, 2000, 1500)
        self.platforms = [
            Platform(0, 1200, 2000, 50),  # Suelo
            Platform(300, 800, 200, 20),
            Platform(600, 700, 200, 20),
            Platform(100, 600, 200, 20),
            Platform(800, 750, 200, 20),
        ]


    def setup_players(self) -> None:
        self.players: List[Player] = [
            Player(100, 100, 50, 50, scene=self, color=(255, 0, 0)),
            Player(200, 100, 50, 50, scene=self, color=(0, 0, 255))
        ]
        self.active_player: Optional[Player] = self.players[0]
        self.hovered_player: Optional[Player] = None

    def setup_camera(self) -> None:
        self.camera = Camera(
            self.game.config.window_width,
            self.game.config.window_height,
            world_bounds=self.world_bounds
        )
        self.camera.follow(self.active_player, deadzone=(50, 50))

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered_player:
                self.active_player = self.hovered_player
                self.camera.follow(self.active_player)

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_player = None
            for player in self.players:
                screen_x = player.x - self.camera.viewport.x
                screen_y = player.y - self.camera.viewport.y
                if (screen_x <= mouse_pos[0] <= screen_x + player.width and
                    screen_y <= mouse_pos[1] <= screen_y + player.height):
                    self.hovered_player = player
                    break

    def update(self, delta_time: float) -> None:
        self.camera.update(delta_time)
        for player in self.players:
            player.update(delta_time)
            
            # Verificar colisiones con plataformas
            for platform in self.platforms:
                if player.collides_with(platform):
                    player.on_collision(platform)  # Maneja la colisión
                    break  # Salir del bucle si hay colisión

            if player == self.hovered_player:
                player.outline_color = (255, 255, 255)
                player.outline_offset += 5*delta_time
            else:
                player.outline_color = None
                player.outline_offset = 2

    def render(self, render_context) -> None:
        render_context.clear()
        for platform in self.platforms:
            platform.render(render_context, camera_offset=(self.camera.viewport.x, self.camera.viewport.y))
        for player in self.players:
            player.render(render_context, camera_offset=(self.camera.viewport.x, self.camera.viewport.y))
