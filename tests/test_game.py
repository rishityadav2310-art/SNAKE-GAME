import unittest
from src.snake import Snake
from src.food import Food

class TestSnakeGameLogic(unittest.TestCase):

    def test_snake_initialization(self):
        snake = Snake(body_parts=3, space_size=20)
        self.assertEqual(len(snake.coordinates), 3)
        self.assertEqual(snake.coordinates[0], [0, 0])

    def test_food_generation_within_bounds(self):
        width, height, space_size = 600, 400, 20
        food = Food(width, height, space_size)
        x, y = food.coordinates
        
        self.assertTrue(0 <= x <= width - space_size)
        self.assertTrue(0 <= y <= height - space_size)
        self.assertEqual(x % space_size, 0)
        self.assertEqual(y % space_size, 0)

if __name__ == "__main__":
    unittest.main()
