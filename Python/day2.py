import sys

class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
    def forward(self, amount: int):
        self.horizontal_position += amount
    def down(self, amount: int):
        self.depth += amount
    def up(self, amount: int):
        self.depth -= amount
    def get_horizontal_position_times_depth(self):
        return self.horizontal_position * self.depth

class BetterSubmarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0
    def forward(self, amount: int):
        self.horizontal_position += amount
        self.depth += (self.aim * amount)
    def down(self, amount: int):
        self.aim += amount
    def up(self, amount: int):
        self.aim -= amount
    def get_horizontal_position_times_depth(self):
        return self.horizontal_position * self.depth


if __name__ == "__main__":
    # Python day2.py < day2_puzzle.txt into cmd prompt
    lines = sys.stdin.readlines()
    instructions = []
    for line in lines:
        split = line.split(' ')
        direction_and_amount = ( str(split[0]), int(split[1]) )
        instructions.append(direction_and_amount)

    # Do both submarine classes with same loop
    sub = Submarine()
    better_sub = BetterSubmarine()
    for instruction in instructions:
        if instruction[0] == "forward":
            sub.forward(instruction[1])
            better_sub.forward(instruction[1])
        if instruction[0] == "down":
            sub.down(instruction[1])
            better_sub.down(instruction[1])
        if instruction[0] == "up":
            sub.up(instruction[1])
            better_sub.up(instruction[1])

    print("Solution one:", sub.get_horizontal_position_times_depth())
    print("Solution two:", better_sub.get_horizontal_position_times_depth())





