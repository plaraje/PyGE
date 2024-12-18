import pygame
import math

class RenderContext:
    def __init__(self, screen, background_color=(135, 206, 235)):
        self.screen = screen
        self.background_color = background_color
        self.width = screen.get_width()
        self.height = screen.get_height()
        self._font_cache = {}

    def clear(self):
        self.screen.fill(self.background_color)

    def draw_rect(self, x, y, width, height, color, filled=True):
        if filled:
            pygame.draw.rect(self.screen, color, (x, y, width, height))
        else:
            pygame.draw.rect(self.screen, color, (x, y, width, height), 2)
    
    def draw_rounded_rect(self, x, y, width, height, color, r: int | list, filled=True):
        if filled:
            if isinstance(r, int):
                pygame.draw.rect(self.screen, color, (x, y, width, height), border_radius=r)
            elif isinstance(r, list):
                if len(r) == 1:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[0],
                                 border_bottom_left_radius=r[0],
                                 border_bottom_right_radius=r[0],
                    )
                elif len(r) == 2:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[0],
                                 border_bottom_left_radius=r[1],
                                 border_bottom_right_radius=r[1],
                    )
                elif len(r) == 4:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[3],
                                 border_bottom_left_radius=r[1],
                                 border_bottom_right_radius=r[2],
                    )
                else:
                    raise ValueError("Invalid length for border_radius list. Expected 1, 2 or 4.")
            else:
                raise TypeError("'border_radius' must be an integer or a list of integers with lenght 1, 2 or 4.")

        else:
            if isinstance(r, int):
                pygame.draw.rect(self.screen, color, (x, y, width, height), 2, border_radius=r)
            elif isinstance(r, list):
                if len(r) == 1:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 2, 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[0],
                                 border_bottom_left_radius=r[0],
                                 border_bottom_right_radius=r[0],
                    )
                elif len(r) == 2:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 2, 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[0],
                                 border_bottom_left_radius=r[1],
                                 border_bottom_right_radius=r[1],
                    )
                elif len(r) == 4:
                    pygame.draw.rect(self.screen, color, (x, y, width, height), 2, 
                                 border_top_left_radius=r[0],
                                 border_top_right_radius=r[3],
                                 border_bottom_left_radius=r[1],
                                 border_bottom_right_radius=r[2],
                    )
                else:
                    raise ValueError("Invalid length for border_radius list. Expected 1, 2 or 4.")
            else:
                raise TypeError("'border_radius' must be an integer or a list of integers with lenght 1, 2 or 4.")

    def draw_rect_alpha(self, x, y, width, height, color):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(surface, color, (0, 0, width, height))
        self.screen.blit(surface, (x, y))

    def draw_circle(self, x, y, radius, color, camera_offset=(0, 0)):
        adjusted_x = x - camera_offset[0]
        adjusted_y = y - camera_offset[1]
        pygame.draw.circle(self.screen, color, (int(adjusted_x), int(adjusted_y)), int(radius))

    def draw_text(self, text, x, y, color=(0, 0, 0), size=24, center=False):
        if size not in self._font_cache:
            self._font_cache[size] = pygame.font.Font(None, size)
        
        font = self._font_cache[size]
        text_surface = font.render(text, True, color)
        
        if center:
            text_rect = text_surface.get_rect(center=(x, y))
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (x, y))

    def draw_parallax_background(self, images, camera_x, camera_y, parallax_factors):
        for img, factor in zip(images, parallax_factors):
            # Calcular posición con efecto parallax
            x = -camera_x * factor
            y = -camera_y * factor * 0.5  # Menor efecto vertical
            
            # Dibujar imagen con tiling horizontal
            img_width = img.get_width()
            start_x = x % img_width - img_width
            
            while start_x < self.width:
                self.screen.blit(img, (start_x, y))
                start_x += img_width

    def flip(self):
        pygame.display.flip()

    def draw_mountains(self, base_y, color, offset_x=0, offset_y=0, height_factor=1.0):
        """
        Dibuja una cadena montañosa usando una función sinusoidal con parallax vertical
        """
        points = [(0, self.height)]
        
        # Generar puntos para la silueta
        for x in range(0, self.width + 50, 10):
            # Usar varias funciones seno para crear un perfil más interesante
            height = (
                math.sin((x + offset_x) * 0.01) * 100 +
                math.sin((x + offset_x) * 0.02) * 50 +
                math.sin((x + offset_x) * 0.005) * 150
            ) * height_factor
            
            # Aplicar offset vertical
            y = base_y - abs(height) + offset_y
            points.append((x, y))
        
        points.append((self.width, self.height))
        pygame.draw.polygon(self.screen, color, points)
