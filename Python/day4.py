import sys

# Below 3 functions create the bingo board


def get_bingo_numbers() -> list[int]:
    bingo_nums_as_string = str(sys.stdin.readline())
    bingo_nums = [int(i) for i in bingo_nums_as_string.split(",")]
    return bingo_nums


def _get_bingo_boards_with_ints() -> list[int]:
    bingo_boards_as_strings = [str(line)[:-1]
                               for line in sys.stdin.readlines()]
    # Last line doesn't have newline char so append the last digit back manually
    bingo_boards_as_strings[-1] += '6'

    all_boards = []
    cur_board = []
    for i in range(1, len(bingo_boards_as_strings)):
        if bingo_boards_as_strings[i] == "":
            all_boards.append(cur_board)
            cur_board = []
        else:
            split = bingo_boards_as_strings[i].split(" ")
            for num in split:
                if num == "":
                    pass
                else:
                    cur_board.append(int(num))
    all_boards.append(cur_board)
    return all_boards


def make_bingo_board_with_bools(bingo_board_of_ints: list[int]) -> list[(int, bool)]:
    num_bool_pair_board = [[bingo_number, False]
                           for bingo_number in bingo_board_of_ints]
    return num_bool_pair_board


# Below functions find the solution

def _check_rows_for_win(board: list, length_of_each_line: int) -> bool:
    # True if a row is all marked as true, otherwise false
    index = 0
    while index < len(board):
        row = board[index:index+length_of_each_line]
        row_win = _check_row_or_column_for_completion(row)
        if (row_win):
            return True
        else:
            index += length_of_each_line
    return False


def _check_columns_for_win(board: list, length_of_each_line: int) -> bool:
    # True if a column is all marked as true, otherwise false
    index = 0
    while index < length_of_each_line:
        column = []
        col_index = index
        while col_index < len(board):
            column.append(board[col_index])
            col_index += length_of_each_line
        column_win = _check_row_or_column_for_completion(column)
        if column_win:
            return True
        else:
            index += 1
    return False


def _check_row_or_column_for_completion(bingo_num_bool_pairs: list) -> bool:
    # Used in the column and row check functions
    for pair in bingo_num_bool_pairs:
        if pair[1] == False:
            return False
    return True


def _check_for_win(bingo_board: list, length_of_each_line: int) -> bool:
    row_win = _check_rows_for_win(bingo_board, length_of_each_line)
    if row_win:
        return True
    column_win = _check_columns_for_win(bingo_board, length_of_each_line)
    if column_win:
        return True
    return False


def _mark_bingo_number_on_board(bingo_board: list, bingo_number: int) -> None:
    for pair in bingo_board:
        if pair[0] == bingo_number:
            pair[1] = True
            return


def _false_values_times_winning_number(bingo_board: list, winning_number: int) -> int:
    false_pairs = []
    for pair in bingo_board:
        if pair[1] == False:
            false_pairs.append(pair[0])
    solution = sum(false_pairs) * winning_number
    return solution


def initialise_bingo_boards_from_stdin() -> list[list[(int, bool)]]:
    bingo_boards_from_file = _get_bingo_boards_with_ints()
    bingo_boards = [make_bingo_board_with_bools(bingo_board)
                    for bingo_board in bingo_boards_from_file]
    return bingo_boards


def get_part_one_solution(bingo_boards: list[list[(int, bool)]], bingo_nums: list[int]) -> int:
    fewest_turns = None
    winning_board = None
    last_num_for_winning_board = None
    # Assumes that at least one board will win
    for bingo_board in bingo_boards:
        win = False
        cur_turns = 0
        for num in bingo_nums:
            cur_turns += 1
            _mark_bingo_number_on_board(bingo_board, num)
            win = _check_for_win(bingo_board, 5)
            if win:
                if fewest_turns == None or fewest_turns > cur_turns:
                    fewest_turns = cur_turns
                    winning_board = bingo_board
                    last_num_for_winning_board = bingo_nums[cur_turns-1]
                break
    solution = _false_values_times_winning_number(
        winning_board, last_num_for_winning_board)
    # print("Fewest turns:", fewest_turns)
    return solution


def get_part_two_solution(bingo_boards: list[list[(int, bool)]], bingo_nums: list[int]) -> int:
    most_turns = None
    losing_board = None
    last_num_for_losing_board = None
    # Assumes that at least one board will win
    for bingo_board in bingo_boards:
        win = False
        cur_turns = 0
        for num in bingo_nums:
            cur_turns += 1
            _mark_bingo_number_on_board(bingo_board, num)
            win = _check_for_win(bingo_board, 5)
            if win:
                if most_turns == None or most_turns < cur_turns:     # < is the only change
                    most_turns = cur_turns
                    losing_board = bingo_board
                    last_num_for_losing_board = bingo_nums[cur_turns-1]
                break
    solution = _false_values_times_winning_number(
        losing_board, last_num_for_losing_board)
    # print("Most turns:", most_turns)
    return solution


def reset_bingo_boards(bingo_boards: list[list[(int, bool)]]) -> None:
    # Sets all True values back to False
    for bingo_board in bingo_boards:
        for pair in bingo_board:
            if pair[1] == True:
                pair[1] = False


if __name__ == "__main__":
    # py day4.py < day4_puzzle.txt into cmd prompt
    bingo_nums = get_bingo_numbers()
    bingo_boards = initialise_bingo_boards_from_stdin()

    solution = get_part_one_solution(bingo_boards, bingo_nums)
    print("Solution one:", solution)

    reset_bingo_boards(bingo_boards)

    solution_two = get_part_two_solution(bingo_boards, bingo_nums)
    print("Solution two:", solution_two)
