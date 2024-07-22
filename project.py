import pygame
from enum import Enum
import random
from datetime import datetime

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class GameState(Enum):
    START = 'START'
    PLAY = 'PLAY'
    GAMEOVER = 'GAMEOVER'


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 10
        self.randomize_position([])

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x, self.y, self.size, self.size))

    def randomize_position(self, snake_body):
        collision = True
        while collision:
            self.x = random.randrange(0, SCREEN_WIDTH, self.size)
            self.y = random.randrange(0, SCREEN_HEIGHT, self.size)
            collision = any(segment.x == self.x and segment.y == self.y for segment in snake_body)

    def check_collision(self, other):
        collision_x = self.x + self.size >= other.pos.x and other.pos.x + other.size >= self.x
        collision_y = self.y + self.size >= other.pos.y and other.pos.y + other.size >= self.y
        return collision_x and collision_y


class Snake:
    def __init__(self):
        self.direction = Direction.RIGHT
        self.pos = pygame.Vector2(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))
        self.length = 3
        self.size = 10
        self.body = [self.pos.copy()]
        for i in range(1, self.length):
            self.body.append(self.pos.copy() - pygame.Vector2(i * 10, 0))

    def move(self):
        if self.direction == Direction.UP:
            self.pos.y -= self.size
            if self.pos.y < 0:
                self.pos.y = SCREEN_HEIGHT
        elif self.direction == Direction.DOWN:
            self.pos.y += self.size
            if self.pos.y > SCREEN_HEIGHT:
                self.pos.y = 0
        elif self.direction == Direction.LEFT:
            self.pos.x -= self.size
            if self.pos.x < 0:
                self.pos.x = SCREEN_WIDTH
        elif self.direction == Direction.RIGHT:
            self.pos.x += self.size
            if self.pos.x > SCREEN_WIDTH:
                self.pos.x = 0

        new_head = self.pos.copy()
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def change_direction(self, new_direction):
        # Ensure the snake cannot reverse
        if new_direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = new_direction
        elif new_direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = new_direction
        elif new_direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = new_direction
        elif new_direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = new_direction

    def check_collision_with_self(self):
        for segment in self.body[1:]:
            if self.pos == segment:
                return True
        return False

    def check_collision_with_food(self, food):
        return food.check_collision(self)

    def grow(self):
        self.length += 1

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, "yellow", (segment.x, segment.y, self.size, self.size))


def reset_game():
    global snake, food, score
    snake = Snake()
    food = Food()
    food.randomize_position(snake.body)
    score = 0


def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, snake, food, score
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    done = False

    # Initialize the snake and food
    reset_game()

    # Initialize game state
    game_state = GameState.START
    enter_pressed = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()

        if game_state == GameState.START:
            screen.fill("black")
            font = pygame.font.Font(None, 74)
            text = font.render("Press Enter to Start", True, "white")
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

            if keys[pygame.K_RETURN] and not enter_pressed:
                enter_pressed = True
            elif not keys[pygame.K_RETURN] and enter_pressed:
                enter_pressed = False
                game_state = GameState.PLAY

        elif game_state == GameState.PLAY:
            if keys[pygame.K_w]:
                snake.change_direction(Direction.UP)
            elif keys[pygame.K_s]:
                snake.change_direction(Direction.DOWN)
            elif keys[pygame.K_a]:
                snake.change_direction(Direction.LEFT)
            elif keys[pygame.K_d]:
                snake.change_direction(Direction.RIGHT)

            # Automatically move the snake
            snake.move()

            # Check for collisions with food
            if snake.check_collision_with_food(food):
                snake.grow()
                score += 1
                food.randomize_position(snake.body)

            # Check for collisions with itself
            if snake.check_collision_with_self():
                game_state = GameState.GAMEOVER

            # Render everything
            screen.fill("black")
            snake.draw(screen)
            food.draw(screen)
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, "white")
            screen.blit(text, (10, 10))

        elif game_state == GameState.GAMEOVER:
            screen.fill("black")
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over", True, "white")
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, "white")
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + text.get_height()))

            text = font.render("Press Enter to Restart", True, "white")
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + text.get_height() * 2))

            if keys[pygame.K_RETURN] and not enter_pressed:
                enter_pressed = True
            elif not keys[pygame.K_RETURN] and enter_pressed:
                enter_pressed = False
                reset_game()
                game_state = GameState.START

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
