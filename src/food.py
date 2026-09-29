import random

class Food:
    def __init__(self, width=600, height=400, space_size=20, color="#FF0000"):
        x = random.randint(0, int((width / space_size) - 1)) * space_size
        y = random.randint(0, int((height / space_size) - 1)) * space_size
        self.coordinates = [x, y]
        self.color = color
