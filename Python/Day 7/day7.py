import sys

crabs = [int(i) for i in str(sys.stdin.readline()).split(",")]


def cheapest_fuel_cost_part_one(crab_list: list[int]) -> tuple[int, int]:
    alignment_pos = None
    cheapest_fuel_cost = None
    for pos in range(0, max(crab_list)):
        fuel_count = 0
        for crab in crab_list:
            difference = abs(crab - pos)
            fuel_count += difference
        if (cheapest_fuel_cost == None) or (fuel_count < cheapest_fuel_cost):
            cheapest_fuel_cost = fuel_count
            alignment_pos = pos

        # Reset count
        fuel_count = 0

    return (cheapest_fuel_cost, alignment_pos)


def triangular_number(number: int) -> int:
    # number should be positive
    return (number * (number + 1)) // 2


def cheapest_fuel_cost_part_two(crab_list: list[int]) -> tuple[int, int]:
    alignment_pos = None
    cheapest_fuel_cost = None
    for pos in range(0, max(crab_list)):
        # print(f"Loop: {pos} of {max(crab_list)}")
        fuel_count = 0
        for crab in crab_list:
            triangular_difference = triangular_number(abs(crab - pos))
            fuel_count += triangular_difference
        if (cheapest_fuel_cost == None) or (fuel_count < cheapest_fuel_cost):
            cheapest_fuel_cost = fuel_count
            alignment_pos = pos

        # Reset count
        fuel_count = 0

    return (cheapest_fuel_cost, alignment_pos)


if __name__ == "__main__":
    solution_one = cheapest_fuel_cost_part_one(crabs)
    print("Solution one:", solution_one)
    solution_two = cheapest_fuel_cost_part_two(crabs)
    print("Solution two:", solution_two)

    # Answer to part 1 is 336040
    # Answer to part 2 is 94813675
