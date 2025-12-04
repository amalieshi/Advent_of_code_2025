from pathlib import Path
from rotations import read_file, rotate, count_zero_clicks

# Problem 1
file_path = Path(__file__).parent / 'data' / 'example2.txt'
instructions = read_file(file_path)
current_position = 50
counter = 0
for instruction in instructions:
    current_position = rotate(current_position, instruction['direction'], instruction['value'])
    if current_position == 0:
        counter += 1
print(f'The answer to problem 1 is: {counter}.')

# Problem 2
instructions = read_file(file_path)
password = count_zero_clicks(instructions)
print(f'The answer to problem 2 is: {password}.')