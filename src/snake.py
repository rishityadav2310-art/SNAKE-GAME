class Snake:
    def __init__(self, body_parts=3, space_size=20, color="#00FF00"):
        self.body_size = body_parts
        self.space_size = space_size
        self.color = color
        self.coordinates = []
        self.squares = []

        for _ in range(0, body_parts):
            self.coordinates.append([0, 0])
