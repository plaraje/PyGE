import pygame

class PlayerController:
    def __init__(self, entity):
        self.entity = entity
        self.game = entity.game
        self.scene = entity.scene
        
        # Configuración de movimiento
        self.move_speed = 300
        self.acceleration = 100
        self.deceleration = 800
        self.jump_force = 200

        # Registrar handlers de input
        self._register_input_handlers()

    def _register_input_handlers(self):
        kb = self.game.keyboard_manager

        # Movimiento horizontal
        kb.add_key_held_handler(pygame.K_a, self._handle_move_left)
        kb.add_key_held_handler(pygame.K_d, self._handle_move_right)
        
        # Salto
        kb.add_key_down_handler(pygame.K_w, self._handle_jump)
        kb.add_key_down_handler(pygame.K_SPACE, self._handle_jump)


    def _handle_move_left(self, delta_time):
        physics = self.entity.physics
        if physics.vx > -self.move_speed:
            physics.vx -= self.acceleration * delta_time

    def _handle_move_right(self, delta_time):
        physics = self.entity.physics
        if physics.vx < self.move_speed:
            physics.vx += self.acceleration * delta_time

    def _handle_jump(self):
        physics = self.entity.physics
        print(f"Jump, isG = {physics.is_grounded}")
        if physics.is_grounded:
            physics.vy = -self.jump_force

    def handle_input(self, delta_time):
        pass