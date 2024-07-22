import pytest
import pygame
from project import Direction, Snake, Food, SCREEN_WIDTH, SCREEN_HEIGHT, reset_game


@pytest.fixture
def snake():
    return Snake()


@pytest.fixture
def food():
    return Food()


def test_move(snake):
    initial_position = snake.pos.copy()
    snake.move()
    assert snake.pos != initial_position


def test_change_direction(snake):
    initial_direction = snake.direction
    snake.change_direction(Direction.UP)
    assert snake.direction == Direction.UP
    snake.change_direction(Direction.DOWN)
    assert snake.direction == Direction.UP  # Should not reverse direction
    snake.change_direction(Direction.LEFT)
    assert snake.direction == Direction.LEFT


def test_grow(snake):
    initial_length = snake.length
    snake.grow()
    assert snake.length == initial_length + 1


def test_randomize_position(food, snake):
    food.randomize_position(snake.body)
    assert 0 <= food.x <= SCREEN_WIDTH - food.size
    assert 0 <= food.y <= SCREEN_HEIGHT - food.size
    for segment in snake.body:
        assert not (food.x == segment.x and food.y == segment.y)


def test_check_collision_with_food(snake, food):
    snake.pos = pygame.Vector2(food.x, food.y)
    assert snake.check_collision_with_food(food)


def test_check_collision_with_self(snake):
    snake.body = [pygame.Vector2(100, 100), pygame.Vector2(110, 100), pygame.Vector2(120, 100)]
    snake.pos = pygame.Vector2(110, 100)  # Position the head at the second segment
    assert snake.check_collision_with_self()
