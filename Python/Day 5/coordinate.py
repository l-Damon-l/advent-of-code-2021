class Coordinate:
    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

    def print(self) -> None:
        print("x:", str(self.x) + ",", "y:", str(self.y))

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y
