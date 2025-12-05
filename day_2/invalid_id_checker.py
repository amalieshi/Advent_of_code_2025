import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace('\n', '')
        ids_list = content.split(',')
    return ids_list

def expand_id(id_range):
    start_id, end_id = id_range.split('-')
    expanded_ids = [str(i) for i in range(int(start_id), int(end_id) + 1)]
    return expanded_ids

def get_invalid_ids(expanded_ids):
    invalid_ids = []
    for i in expanded_ids:
        length = len(i)
        mid_length = int(length / 2)
        first_half = i[:mid_length]
        second_half = i[mid_length:]
        if first_half == second_half:
            invalid_ids.append(i)
    return invalid_ids

def get_new_invalid_ids(expanded_ids):
    invalid_ids = []
    for i in expanded_ids:
        length = len(i)
        for j in range(1, length):
            parts = length / j
            if parts.is_integer():
                parts = int(parts)
                segments = [i[k * j:(k + 1) * j] for k in range(parts)]
                if all(segment == segments[0] for segment in segments):
                    invalid_ids.append(i)
                    break
    return invalid_ids

def add_up_all_invalid_ids(invalid_id_list):
    total = sum(int(i) for i in invalid_id_list)
    return total



