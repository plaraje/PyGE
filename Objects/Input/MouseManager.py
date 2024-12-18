import pygame

class MouseManager:
    def __init__(self):
        self.position = (0, 0)
        self.buttons = {
            1: False,  # Botón izquierdo
            2: False,  # Botón medio
            3: False   # Botón derecho
        }
        self.click_handlers = {}
        self.release_handlers = {}
        self.drag_handlers = {}
        self.move_handlers = []
        self.dragging = False
        self.drag_start = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.position = event.pos
            self._handle_motion(event)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons[event.button] = True
            self._handle_click(event)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.buttons[event.button] = False
            self._handle_release(event)

    def update(self, delta_time):
        # Actualizar estado de arrastre
        if self.dragging:
            for button in self.drag_handlers:
                if self.buttons[button]:
                    for handler in self.drag_handlers[button]:
                        handler(self.position, self.drag_start)

    def _handle_motion(self, event):
        for handler in self.move_handlers:
            handler(event.pos)
        
        if any(self.buttons.values()):
            if not self.dragging:
                self.dragging = True
                self.drag_start = event.pos

    def _handle_click(self, event):
        if event.button in self.click_handlers:
            for handler in self.click_handlers[event.button]:
                handler(event.pos)

    def _handle_release(self, event):
        if event.button in self.release_handlers:
            for handler in self.release_handlers[event.button]:
                handler(event.pos)
        
        if self.dragging:
            self.dragging = False
            self.drag_start = None

    def add_click_handler(self, button, handler):
        if button not in self.click_handlers:
            self.click_handlers[button] = []
        self.click_handlers[button].append(handler)

    def add_release_handler(self, button, handler):
        if button not in self.release_handlers:
            self.release_handlers[button] = []
        self.release_handlers[button].append(handler)

    def add_drag_handler(self, button, handler):
        if button not in self.drag_handlers:
            self.drag_handlers[button] = []
        self.drag_handlers[button].append(handler)

    def add_move_handler(self, handler):
        self.move_handlers.append(handler)

    def remove_handler(self, handler):
        # Remover de todos los tipos de handlers
        for button in self.click_handlers:
            if handler in self.click_handlers[button]:
                self.click_handlers[button].remove(handler)
                
        for button in self.release_handlers:
            if handler in self.release_handlers[button]:
                self.release_handlers[button].remove(handler)
                
        for button in self.drag_handlers:
            if handler in self.drag_handlers[button]:
                self.drag_handlers[button].remove(handler)
                
        if handler in self.move_handlers:
            self.move_handlers.remove(handler)

    def get_position(self):
        return self.position

    def is_button_pressed(self, button):
        return self.buttons.get(button, False)

    def is_dragging(self):
        return self.dragging
