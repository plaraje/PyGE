from .UIElement import UIElement

class Panel(UIElement):
    def __init__(self, x, y, width, height, color=(100, 100, 100, 200)):
        super().__init__(x, y, width, height)
        self.color = color

    def render(self, render_context):
        if not self.visible:
            return
            
        x, y = self.get_absolute_position()
        render_context.draw_rect_alpha(x, y, self.width, self.height, self.color)
        super().render(render_context)
