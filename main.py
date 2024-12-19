from Objects import Game
from Example.Scenes import MainMenuScene, GameScene
def run_example():
    game = Game()
    menu = MainMenuScene(game)
    games = GameScene(game)
    game.set_scene(menu)
    game.run()

if __name__ == "__main__":
    run_example()
