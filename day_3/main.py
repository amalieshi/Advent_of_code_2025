from pathlib import Path

from day_3.joltage_ratings import get_largest_joltage, get_new_largest_joltage
from joltage_ratings import (read_files)

if __name__ == '__main__':
    filepath = Path(__file__).parent/ 'data' / 'example2.txt'

    # Problem 1
    joltage_data = read_files(filepath)
    all_joltage_data = []
    for joltage in joltage_data:
        print(f'The {joltage} produces {get_largest_joltage(joltage)}')
        all_joltage_data.append(get_largest_joltage(joltage))
    total_output = sum(all_joltage_data)
    print(f'The station produces a total of {total_output} joltages.')

    # Problem 2
    print('\nProblem 2 Results:\n')
    joltage_data = read_files(filepath)
    all_joltage_data = []
    for joltage in joltage_data:
        print(f'The {joltage} produces {get_new_largest_joltage(joltage)}')
        all_joltage_data.append(get_new_largest_joltage(joltage))
    total_output = sum(all_joltage_data)
    print(f'The station produces a total of {total_output} joltages.')