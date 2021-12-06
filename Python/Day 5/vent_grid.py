from coordinate import Coordinate


class VentGrid:
    def __init__(self, row_length: int, column_length: int) -> None:
        self.row_length = row_length
        self.column_length = column_length
        self.grid = self._initialise_grid(row_length, column_length)
        self.overlaps = 0

    def _initialise_grid(self, row_length: int, column_length: int) -> list[list[str]]:
        grid = []
        current_row = []
        for _ in range(column_length):
            for _ in range(row_length):
                current_row.append('.')
            grid.append(current_row)
            current_row = []
        return grid

    def mark_pos_on_grid(self, row_number: int, column_number: int) -> None:
        if self.grid[row_number][column_number] == '.':
            self.grid[row_number][column_number] = 1
        elif self.grid[row_number][column_number] == 1:
            # An overlap has occurred
            self.grid[row_number][column_number] += 1
            self.overlaps += 1
        else:
            self.grid[row_number][column_number] += 1

    def mark_line_on_grid(self, first_coordinate: Coordinate, second_coordinate: Coordinate) -> None:
        cur_x = first_coordinate.get_x()
        cur_y = first_coordinate.get_y()
        x_destination = second_coordinate.get_x()
        y_destination = second_coordinate.get_y()

        # If neither the x value or y value between each coordinate is equal, return (couldn't be a straight line)
        # This line is the only difference between the class for part one and part two
        if not ((cur_x == x_destination) or (cur_y == y_destination)):
            return

        self.mark_pos_on_grid(cur_x, cur_y)
        while (cur_x != x_destination) or (cur_y != y_destination):
            if cur_x < x_destination:
                cur_x += 1
            elif cur_x > x_destination:
                cur_x -= 1
            if cur_y < y_destination:
                cur_y += 1
            elif cur_y > y_destination:
                cur_y -= 1
            self.mark_pos_on_grid(cur_x, cur_y)

    def get_num_of_overlaps(self) -> int:
        return self.overlaps

    def print_grid(self):
        # Prints the grid nicely (evenly spaced)
        print('\n')
        for row in self.grid:
            print(*row)
        print('\n')
