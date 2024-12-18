from .UIElement import UIElement
import pygame

class Button(UIElement):
    def __init__(self, x, y, width, height, text, callback=None, normal_color=(100, 100, 100), hover_color=(120, 120, 120), pressed_color=(80, 80, 80), text_color=(255, 255, 255), font_size=24):
        super().__init__(x, y, width, height)
        self.text = text
        self.callback = callback
        self.hovered = False
        self.pressed = False
        self.normal_color = normal_color
        self.hover_color = hover_color 
        self.pressed_color = pressed_color
        self.text_color = text_color
        self.font_size = font_size

    def handle_event(self, event):
        if not self.visible or not self.enabled:
            return False

        x, y = self.get_absolute_position()
        
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (x <= event.pos[0] <= x + self.width and 
                          y <= event.pos[1] <= y + self.height)
            return self.hovered
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered:
                self.pressed = True
                return True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.pressed:
                self.pressed = False
                if self.hovered and self.callback:
                    self.callback()
                return True
                
        return False

    def render(self, render_context):
        if not self.visible:
            return

        x, y = self.get_absolute_position()
        color = self.pressed_color if self.pressed else (
            self.hover_color if self.hovered else self.normal_color
        )
        
        render_context.draw_rect(x, y, self.width, self.height, color)
        render_context.draw_text(
            self.text, 
            x + self.width/2, 
            y + self.height/2, 
            self.text_color,
            self.font_size,
            center=True
        )
        
        super().render(render_context)
