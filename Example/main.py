from Objects import Game
from Example.Scenes.MainMenuScene import MainMenuScene
from Example.Scenes.GameScene import GameScene

def run_example():
    game = Game()
    menu = MainMenuScene(game)
    games = GameScene(game)
    game.set_scene(menu)
    game.run()

if __name__ == "__main__":
    run_example()
