

class OctopusGrid:

    def __init__(self, row_list: list[list[int]]) -> None:
        self.grid = row_list
        self.grid_length = len(self.grid[0])  # The grid is square
        self.flashes = 0
        self.steps = 0
        self.found_part_two_solution = False

    def grid_step(self) -> None:
        self.steps += 1

        # Increment everything by 1
        for i in range(0, self.grid_length):  # row
            for j in range(0, self.grid_length):  # column
                self.grid[i][j] += 1
        all_digits_under_ten = False

        # Flash any digits over 9
        while not all_digits_under_ten:
            found_digit_above_9 = False
            for i in range(0, self.grid_length):  # row
                for j in range(0, self.grid_length):
                    if self.grid[i][j] > 9:
                        found_digit_above_9 = True
                        self._flash_node_start(i, j)
            if not found_digit_above_9:
                all_digits_under_ten = True

    def _flash_node_start(self, row: int, col: int) -> None:

        flashed_nodes = []

        def _flash_node(row: int, col: int) -> None:

            self.grid[row][col] = 0
            flashed_nodes.append(self.grid[row][col])

            # Below should have all been contained in a loop...

            # Top-left
            if (row - 1) >= 0 and (col - 1) >= 0 and (self.grid[row-1][col-1]) not in flashed_nodes:
                self.grid[row-1][col-1] += 1
                if self.grid[row-1][col-1] > 9:
                    _flash_node(row-1, col-1)
            # Top
            if (row - 1) >= 0 and (self.grid[row-1][col]) not in flashed_nodes:
                self.grid[row-1][col] += 1
                if self.grid[row-1][col] > 9:
                    _flash_node(row-1, col)
            # Top-right
            if (row - 1) >= 0 and (col + 1) <= self.grid_length - 1 and (self.grid[row-1][col+1]) not in flashed_nodes:
                self.grid[row-1][col+1] += 1
                if self.grid[row-1][col+1] > 9:
                    _flash_node(row-1, col+1)
            # Right
            if (col + 1) <= self.grid_length - 1 and (self.grid[row][col+1]) not in flashed_nodes:
                self.grid[row][col+1] += 1
                if self.grid[row][col+1] > 9:
                    _flash_node(row, col+1)
            # Bottom-right
            if (row + 1) <= self.grid_length - 1 and (col + 1) <= self.grid_length - 1 and (self.grid[row+1][col+1]) not in flashed_nodes:
                self.grid[row+1][col+1] += 1
                if self.grid[row+1][col+1] > 9:
                    _flash_node(row+1, col+1)
            # Bottom
            if (row + 1) <= self.grid_length - 1 and (self.grid[row+1][col]) not in flashed_nodes:
                self.grid[row+1][col] += 1
                if self.grid[row+1][col] > 9:
                    _flash_node(row+1, col)
            # Bottom-left
            if (row + 1) <= self.grid_length - 1 and (col - 1) >= 0 and (self.grid[row+1][col-1]) not in flashed_nodes:
                self.grid[row+1][col-1] += 1
                if self.grid[row+1][col-1] > 9:
                    _flash_node(row+1, col-1)
            # Left
            if (col - 1) >= 0 and (self.grid[row][col-1]) not in flashed_nodes:
                self.grid[row][col-1] += 1
                if self.grid[row][col-1] > 9:
                    _flash_node(row, col-1)

        _flash_node(row, col)

        # For part 2 (When all the nodes flash simultaneously)
        if len(flashed_nodes) == (self.grid_length * self.grid_length):
            self.found_part_two_solution = True

        self.flashes += len(flashed_nodes)

    def print_grid(self) -> None:
        # Prints the grid nicely (evenly spaced)
        print('\n')
        for row in self.grid:
            print(*row)
        print('\n')
