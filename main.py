from Example.Scenes.GameScene import GameScene
from Objects import Game

def run_game():
    game = Game()
    game.set_scene(GameScene(game))
    game.run()

if __name__ == "__main__":
    run_game()
