import sys

MATCHING_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
ERROR_SCORES_PART_TWO = {")": 1, "]": 2, "}": 3, ">": 4}


indexes_to_remove_after_part_one = []


def syntaxScore(string_list: list[str]):
    index = 0  # For part 2
    score = 0
    for string in string_list:
        open_symbols = []
        for char in string:
            if char in '([{<':
                open_symbols.append(char)
            else:
                if MATCHING_PAIRS[open_symbols.pop()] != char:
                    score += ERROR_SCORES[char]
                    # Bit clumsy but whatever (for part 2)
                    indexes_to_remove_after_part_one.append(
                        index)
                    # Go to next string (after index += 1)
                    break
        index += 1
    return score


def new_list_without_error_strings(string_list: list[str], unwanted_indexes: list[int]):
    new_list = []
    for i in range(0, len(string_list)):
        if i in unwanted_indexes:
            pass
        else:
            new_list.append(string_list[i])
    return new_list


def _score_incomplete_string_solution(string_list: list[str]):
    score = 0
    for char in string_list:
        score *= 5
        score += ERROR_SCORES_PART_TWO[char]
    return score


def create_score_list_for_incomplete_strings(string_list: list[str]):
    score_list = []
    for string in string_list:
        open_symbols = []
        chars_to_complete_string = []
        for char in string:
            if char in '([{<':
                open_symbols.append(char)
            else:
                open_symbols.pop()
        for i in range(len(open_symbols) - 1, -1, -1):
            chars_to_complete_string.append(MATCHING_PAIRS[open_symbols[i]])
        # print(completion_chars)
        score = _score_incomplete_string_solution(chars_to_complete_string)
        score_list.append(score)
    return score_list


def get_median_score(score_list: list[int]):
    score_list.sort()
    if len(score_list) % 2 == 0:
        # Get the average of the 2 middle values
        index_one = len(score_list) // 2
        index_two = index_one - 1
        return (score_list[index_one] + score_list[index_two]) / 2
    else:
        return score_list[len(score_list) // 2]


def main():
    # py day10.py < day10_puzzle.txt into cmd prompt
    test_lines = [str(line.strip()) for line in sys.stdin.readlines()]

    solution_one = syntaxScore(test_lines)
    print("Solution one:", solution_one)

    # New list of only the non-corrupt strings
    incomplete_strings = new_list_without_error_strings(
        test_lines, indexes_to_remove_after_part_one)
    score_list = create_score_list_for_incomplete_strings(incomplete_strings)
    solution_two = get_median_score(score_list)
    print("Solution two:", solution_two)


if __name__ == "__main__":
    main()

    # Answer to part 1 is 392139
    # Answer to part 2 is 4001832844
