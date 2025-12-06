from itertools import combinations

def read_files(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        numbers = [line.replace('\n', '').strip() for line in lines]
    return numbers

def get_largest_joltage(joltage_sequence):
    '''Get the largest joltage from a numerical sequence.'''
    largest_joltage = 0
    for i in range(len(joltage_sequence)):
        for j in range(i + 1, len(joltage_sequence)):
            joltage = int(joltage_sequence[i] + joltage_sequence[j])
            if joltage > largest_joltage:
                largest_joltage = joltage
    final_joltage = largest_joltage
    return final_joltage


# def get_new_largest_joltage(joltage_sequence):
#     largest_joltage = 0
#     indices = range(len(joltage_sequence))
#     for combo in combinations(indices, 12):
#         seq = ''.join(joltage_sequence[i] for i in combo)
#         joltage = int(seq)
#         if joltage > largest_joltage:
#             largest_joltage = joltage
#     return largest_joltage

def get_new_largest_joltage(joltage_sequence):
    # Convert to list of digits for easier manipulation
    digits = list(joltage_sequence)
    result = []

    # For each position in the 12-digit result
    for pos in range(12):
        # Find the largest digit we can place at this position
        # while ensuring we have enough digits left for remaining positions
        remaining_positions = 12 - pos - 1
        min_remaining_digits = len(digits) - remaining_positions

        # Find the largest digit among the first min_remaining_digits digits
        best_digit = '0'
        best_index = -1

        for i in range(min(len(digits), min_remaining_digits)):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_index = i

        # Add the best digit to result and remove it from available digits
        result.append(best_digit)
        digits.pop(best_index)

    return int(''.join(result))

