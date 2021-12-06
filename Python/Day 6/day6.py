import sys
from collections import OrderedDict


lanternfish_list = [int(i) for i in str(sys.stdin.readline()).split(",")]


def _count_dict(dictionary: dict) -> int:
    # Gets amount of fish in the dictionary
    size = 0
    for (_, val) in dictionary.items():
        size += val
    return size


def simulate_lanternfish(lanternfish: list[int], num_days: int) -> list[int]:
    # Initialise dict
    dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in lanternfish:
        dictionary[fish] += 1

    for day in range(num_days):
        # print("Day:", day)
        temp_val = dictionary[0]
        dictionary[0] = 0
        for i in range(1, 9):
            dictionary[i-1] += dictionary[i]
            dictionary[i] = 0
        dictionary[8] += temp_val
        dictionary[6] += temp_val
    return _count_dict(dictionary)


if __name__ == "__main__":
    # py day6.py < day6_puzzle.txt into cmd prompt

    solution_one = simulate_lanternfish(lanternfish_list, 80)
    print("Solution one:", solution_one)
    solution_two = simulate_lanternfish(lanternfish_list, 256)
    print("Solution two:", solution_two)

    # Answer to part 1 is 380612
    # Answer to part 2 is 1710166656900
