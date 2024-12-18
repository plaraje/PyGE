from typing import Dict, Any, Callable

from Objects.Core.RenderContext import RenderContext

class DebugInfo:
    def __init__(self):
        self.values: Dict[str, Callable[[], Any]] = {}
        self.visible = False
        self.font_size = 16
        self.color = (255, 255, 255)
        self.padding = 10

    def add_value(self, name: str, getter: Callable[[], Any]) -> None:
        self.values[name] = getter

    def remove_value(self, name: str) -> None:
        if name in self.values:
            del self.values[name]

    def render(self, render_context: 'RenderContext') -> None:
        if not self.visible:
            return

        y = self.padding
        for name, getter in self.values.items():
            value = getter()
            text = f"{name}: {value}"
            render_context.draw_text(
                text,
                self.padding,
                y,
                self.color,
                self.font_size,
                center=False
            )
            y += self.font_size + 5
