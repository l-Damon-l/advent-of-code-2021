import sys
import math

def depth_increases(depths: list[int]) -> int:
    increases = 0
    for i in range (0, len(depths) - 1):
        if depths[i] < depths[i+1]:
            increases += 1
    return increases

def depth_increases_sliding_windows(depths: list[int]) -> int:
    increases = 0
    prev_window = math.inf
    for i in range(1, len(depths) - 1):
        window = (depths[i-1] + depths[i] + depths[i+1])
        if (window > prev_window):
            increases += 1
        prev_window = window 
    return increases

if __name__ == "__main__":
    # python day1.py < day1_puzzle.txt into cmd promt
    lines = sys.stdin.readlines()
    depths = [int(line) for line in lines]
    solution = depth_increases(depths)
    print("First solution:", solution)

    solution_two = depth_increases_sliding_windows(depths)
    print ("Second solution:", solution_two)