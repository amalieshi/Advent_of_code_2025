def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        steps = content.splitlines()
    instructions = []
    for idx, step in enumerate(steps):
        direction = step[0]
        value = int(step[1:])
        instructions.append({
            'index': idx,
            'direction': direction,
            'value': value
        })
    return instructions

def rotate(current_position, turn_direction, value):
    if turn_direction == 'L':
        # Move left (toward lower numbers), wrap around
        return (current_position - value) % 100
    elif turn_direction == 'R':
        # Move right (toward higher numbers), wrap around
        return (current_position + value) % 100
    else:
        raise ValueError("Invalid direction")

def count_zero_clicks(instructions, start_position=50):
    zero_count = 0
    position = start_position
    for instr in instructions:
        direction = instr['direction']
        value = instr['value']
        if direction == 'L':
            # Moving left: decreasing position
            # Number of times 0 is passed
            passes = ((position - value) // 100) - (position // 100)
            # Calculate all positions passed
            for i in range(1, value + 1):
                if (position - i) % 100 == 0:
                    zero_count += 1
            position = (position - value) % 100
        else:
            # Moving right: increasing position
            for i in range(1, value + 1):
                if (position + i) % 100 == 0:
                    zero_count += 1
            position = (position + value) % 100
    return zero_count
