import pygame

class KeyboardManager:
    def __init__(self):
        self.pressed_keys = {}
        self.key_down_handlers = {}
        self.key_up_handlers = {}
        self.key_held_handlers = {}

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.pressed_keys[event.key] = True
            if event.key in self.key_down_handlers:
                for handler in self.key_down_handlers[event.key]:
                    handler()
                    
        elif event.type == pygame.KEYUP:
            self.pressed_keys[event.key] = False
            if event.key in self.key_up_handlers:
                for handler in self.key_up_handlers[event.key]:
                    handler()

    def update(self, delta_time):
        # Manejar teclas mantenidas
        for key in self.pressed_keys:
            if self.pressed_keys[key] and key in self.key_held_handlers:
                for handler in self.key_held_handlers[key]:
                    handler(delta_time)

    def is_key_pressed(self, key):
        return self.pressed_keys.get(key, False)

    def add_key_down_handler(self, key, handler):
        if key not in self.key_down_handlers:
            self.key_down_handlers[key] = []
        self.key_down_handlers[key].append(handler)

    def add_key_up_handler(self, key, handler):
        if key not in self.key_up_handlers:
            self.key_up_handlers[key] = []
        self.key_up_handlers[key].append(handler)

    def add_key_held_handler(self, key, handler):
        if key not in self.key_held_handlers:
            self.key_held_handlers[key] = []
        self.key_held_handlers[key].append(handler)

    def remove_key_handler(self, key, handler):
        if key in self.key_down_handlers and handler in self.key_down_handlers[key]:
            self.key_down_handlers[key].remove(handler)
        if key in self.key_up_handlers and handler in self.key_up_handlers[key]:
            self.key_up_handlers[key].remove(handler)
        if key in self.key_held_handlers and handler in self.key_held_handlers[key]:
            self.key_held_handlers[key].remove(handler)
