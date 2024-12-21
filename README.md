# PyGE

PyGE is a object-oriented game engine made in python and pygame, it is made to work with the last versions of python and pygame.
To run the demo, just clone this repository, install pygame with `pip install pygame` and run the main.py file in the root folder.


## Features

- **Scene Management**: Easily switch between different game scenes such as the main menu, game scene, and pause menu.
- **Entity System**: Manage game entities like players, enemies, and platforms with ease.
- **UI Components**: Built-in support for UI elements like buttons, panels, and labels.
- **Debugging Tools**: Integrated debugging information display to monitor game performance and entity states.
- **Particle System**: Create dynamic particle effects for enhanced visual feedback.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/plaraje/PyGE.git
   ```

2. Navigate to the project directory:

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Game

To start the game, run the following command:

```bash
python main.py
```

### Game Structure

- **Scenes**: The game is divided into different scenes. Each scene is a subclass of the `Scene` class and is responsible for its own setup, update, and rendering logic.
  - `GameScene`: The main gameplay scene where entities are managed, and game logic is executed.
  - `MainMenuScene`: The initial scene displayed when the game starts, allowing players to start the game or quit.

- **Entities**: Entities such as `Player`, `Enemy`, and `Platform` are managed within the `GameScene`. They are responsible for their own behavior and interactions.

- **UI Components**: UI elements are managed using the `UIManager`. The pause menu and debug information are examples of UI components used in the game.

- **Debugging**: The game includes a `DebugInfo` class to monitor various game metrics like FPS and player position. This can be toggled on and off using the pause menu.

### Key Bindings

- `ESC`: Toggle pause menu
- `W`, `A`, `S`, `D`: Player movement controls
- `R`: Restart the game

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.


## Screenshots
![main menu](/Screenshots/MainMenu.png)
![game](/Screenshots/Gameplay.png)
![pause](/Screenshots/PauseMenu.png)
