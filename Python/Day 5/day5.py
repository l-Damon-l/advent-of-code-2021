import sys

from vent_grid import VentGrid
from vent_grid_two import VentGridTwo
from coordinate import Coordinate


# Turn the input txt file into a list of tuples with each coordinate contained
def get_coordinate_inputs() -> list[(Coordinate, Coordinate)]:
    input_lines_as_strs = [str(line) for line in sys.stdin.readlines()]
    coordinates_as_list = []
    for line in input_lines_as_strs:
        split = line.split(" -> ")
        first_x_and_y = split[0].split(",")
        second_x_and_y = split[1].split(",")
        first_coordinate = Coordinate(
            int(first_x_and_y[0]), int(first_x_and_y[1]))
        second_coordinate = Coordinate(
            int(second_x_and_y[0]), int(second_x_and_y[1]))
        coordinates_as_list.append((first_coordinate, second_coordinate))
    return coordinates_as_list


# Get the largest of x and y from all the coordinates in the list
# This is used to create the grid at the correct size
def get_max_x_and_max_y(coordinate_list: list[(Coordinate, Coordinate)]) -> tuple[int, int]:
    max_x = 0
    max_y = 0
    for coordinate_pair in coordinate_list:
        # Check if x bigger than current max x
        if coordinate_pair[0].get_x() > max_x:
            max_x = coordinate_pair[0].get_x()
            if coordinate_pair[1].get_x() > max_x:
                max_x = coordinate_pair[1].get_x()
        # Check if y bigger than current max y
        if coordinate_pair[0].get_y() > max_y:
            max_y = coordinate_pair[0].get_y()
            if coordinate_pair[1].get_y() > max_y:
                max_y = coordinate_pair[1].get_y()
    return (max_x, max_y)


if __name__ == "__main__":
    # py < day5.py < day5_puzzle.txt into cmd prompt
    coordinate_inputs = get_coordinate_inputs()
    max_x, max_y = get_max_x_and_max_y(coordinate_inputs)

    grid = VentGrid(max_x + 1, max_y + 1)
    # Mark all the lines from the coordinates on the grid (when applicable)
    for coordinate_pair in coordinate_inputs:
        grid.mark_line_on_grid(coordinate_pair[0], coordinate_pair[1])

    solution_one = grid.get_num_of_overlaps()
    print("Solution one:", solution_one)

    part_two_grid = VentGridTwo(max_x + 1, max_y + 1)
    # Mark all the lines from the coordinates on the grid (including diagonals)
    for coordinate_pair in coordinate_inputs:
        part_two_grid.mark_line_on_grid(coordinate_pair[0], coordinate_pair[1])

    solution_two = part_two_grid.get_num_of_overlaps()
    print("Solution two:", solution_two)

    # Answer to part one is 4421
    # Answer to part two is 18674
