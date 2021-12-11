import sys
from octupus_grid import OctopusGrid


def handle_input() -> list[list[int]]:
    lines = [str(s).strip() for s in sys.stdin.readlines()]
    grid = []
    for line in lines:
        cur_line = []
        for digit in line:
            cur_line.append(int(digit))
        grid.append(cur_line)
    return grid


def main():
    grid_input = handle_input()

    # Number of flashes after 100 steps
    octopus_grid = OctopusGrid(grid_input)
    for i in range(100):
        octopus_grid.grid_step()
    print("Solution one:", octopus_grid.flashes)

    # How many steps until all nodes flash simulatneously
    while not octopus_grid.found_part_two_solution:
        octopus_grid.grid_step()  # Prints solution from class
    print("Solution two:", octopus_grid.steps)


if __name__ == "__main__":
    main()
