from Objects import Game
from Example.Scenes.GameScene import GameScene

def run_example():
    game = Game()
    game.set_scene(GameScene(game))
    game.run()

if __name__ == "__main__":
    run_example()
