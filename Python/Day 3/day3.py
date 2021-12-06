import sys

def calc_gamma(bits: list[str]) -> str:
    gamma = ""
    zeros = 0
    ones = 0
    # Each binary string must be the same length
    for row in range(0, len(bits[0])):
        for column in range(0, len(bits) - 1):
            if bits[column][row] == "0":
                zeros += 1
            elif bits[column][row] == "1":
                ones += 1
        if zeros > ones:
            gamma += "0"
        else:
            gamma += "1"
        zeros = ones = 0
    return gamma


def calc_epsilon_from_gamma(gamma: str) -> str:
    epsilon = ""
    for bit in gamma:   
        if bit == "0":
            epsilon += "1"
        else: 
            epsilon += "0"
    return epsilon


def calc_oxygen_generator_rating(bits: list[str]) -> str:
    # Assume there is only 1 possible string to return
    zeros = []
    ones = []
    valid_bits = bits
    # Each binary string must be the same length
    for row in range(0, len(valid_bits[0])):
        for column in range(0, len(valid_bits)):
            if valid_bits[column][row] == "0":
                zeros.append(valid_bits[column])
            elif valid_bits[column][row] == "1":
                ones.append(valid_bits[column])
        if len(zeros) <= len(ones):
            valid_bits = ones
        else:
            valid_bits = zeros

        # Reset lists, break from loop if solution is found
        zeros = []
        ones = []
        if len(valid_bits) == 1:
            break

    if len(valid_bits) == 1:
        return valid_bits[0]
    else:
        return "Problem"


def calc_co2_scrubber_rating(bits: list[str]) -> str:
    # Assume there is only 1 possible string to return
    zeros = []
    ones = []
    valid_bits = bits
    # Each binary string must be the same length
    for row in range(0, len(valid_bits[0])):
        for column in range(0, len(valid_bits)):
            if valid_bits[column][row] == "0":
                zeros.append(valid_bits[column])
            elif valid_bits[column][row] == "1":
                ones.append(valid_bits[column])
        if len(zeros) <= len(ones):
            valid_bits = zeros
        else:
            valid_bits = ones
        
        # Reset lists, break from loop if solution is found
        zeros = []
        ones = []
        if len(valid_bits) == 1:
            break
    
    if len(valid_bits) == 1:
        return valid_bits[0]
    else:
        return "Problem"


if __name__ == "__main__":
    # python day3.py < day3_puzzle.txt into cmd prompt
    lines = sys.stdin.readlines()
    bits = [str(line)[:-1] for line in lines]    # [:-1] removes \n at end of each line

    gamma = calc_gamma(bits)
    epsilon = calc_epsilon_from_gamma(gamma)
    solution_one = int(gamma, 2) * int(epsilon, 2)
    print ("Solution one:", solution_one)

    oxygen_generator_rating = calc_oxygen_generator_rating(bits)
    co2_scrubber_rating = calc_co2_scrubber_rating(bits)
    solution_two = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print("Solution two:", solution_two)


