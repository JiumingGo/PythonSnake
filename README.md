# Snake 
#### Description:

This project is a classic implementation of the Snake game using Python and the Pygame library. The game involves controlling a snake to eat food that appears randomly on the screen. As the snake eats the food, it grows longer, and the player's score increases. The objective is to avoid colliding with the snake's own body, as doing so results in a game over.

## Project Structure

### 1. project.py
This file contains the main game logic and class definitions for the Snake game. The key components include:

- **Direction Enum**: Defines the possible directions the snake can move (UP, DOWN, LEFT, RIGHT).
- **GameState Enum**: Defines the possible states of the game (START, PLAY, GAMEOVER).
- **Food Class**: Manages the food objects, including their position and collision detection with the snake.
- **Snake Class**: Manages the snake's properties, movement, direction changes, growth, and collision detection with food and itself.
- **reset_game Function**: Resets the game state, including the snake, food, and score.
- **main Function**: Initializes Pygame, sets up the game window, handles the game loop, and manages state transitions.

### 2. test_project.py
This file contains the unit tests for the functions in `project.py`. The tests are written using the pytest framework and include:

- **test_move**: Ensures that the snake moves from its initial position.
- **test_change_direction**: Validates that the snake's direction changes correctly and doesn't reverse.
- **test_grow**: Confirms that the snake's length increases when it grows.
- **test_randomize_position**: Checks that the food's position is randomized correctly and does not overlap with the snake's body.
- **test_check_collision_with_food**: Ensures that the snake correctly detects a collision with the food.
- **test_check_collision_with_self**: Verifies that the snake detects a collision with itself when it overlaps.

### 3. requirements.txt
This file lists the pip-installable libraries required by the project. For this project, the dependencies are:
- pygame
- pytest


### Design Choices and Considerations
1. **Game State Management**:
    - The game uses an enum `GameState` to manage different states of the game (START, PLAY, GAMEOVER). This helps in structuring the game flow and handling transitions between states cleanly.

2. **Direction and Movement**:
    - The snake's movement and direction are managed using the `Direction` enum. This ensures that the direction is easily manageable and extensible.

3. **Collision Detection**:
    - The `Food` class includes methods to check for collisions with the snake. This ensures that the food does not spawn inside the snake's body.
    - The `Snake` class includes methods to check for collisions with its own body, which triggers the game over state.

4. **Random Food Placement**:
    - The `Food` class has a method to randomize its position on the screen. It ensures that the new position does not collide with the snake’s body, making the gameplay fair and challenging.

5. **Testing**:
    - Unit tests are written using the pytest framework to ensure the core functionalities of the game are working correctly. This includes testing the snake's movement, direction changes, growth, and collision detection.

### Future Improvements
1. **Enhanced Graphics**:
    - Adding more visual elements and animations to make the game visually appealing.

2. **Sound Effects**:
    - Integrating sound effects for actions like eating food and game over to enhance the player experience.

3. **Advanced Levels**:
    - Introducing different levels with varying difficulty, such as increasing the speed of the snake or adding obstacles.

4. **High Scores**:
    - Implementing a feature to save and display high scores, encouraging players to improve their performance.
