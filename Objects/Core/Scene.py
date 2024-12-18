# Objects/Scenes/Scene.py
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from Objects.Core.Game import Game
    from Objects.Core.RenderContext import RenderContext

class Scene:
    def __init__(self, game: 'Game') -> None:
        self.game: 'Game' = game

    def handle_event(self, event: 'pygame.event.Event') -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def fixed_update(self, fixed_delta: float) -> None:
        pass

    def render(self, render_context: 'RenderContext') -> None:
        pass