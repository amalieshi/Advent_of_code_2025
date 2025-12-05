from pathlib import Path

from invalid_id_checker import (
    read_file,
    expand_id,
    get_invalid_ids,
    get_new_invalid_ids,
    add_up_all_invalid_ids)





if __name__ == '__main__':
    # Problem 1
    file_path = Path(__file__).parent / 'data' / 'example2.txt'
    id_list = read_file(file_path)
    invalid_id_list = []
    for id_range in id_list:
        expanded_ids = expand_id(id_range)
        list = get_invalid_ids(expanded_ids)
        invalid_id_list.extend(list)
    sum = add_up_all_invalid_ids(invalid_id_list)
    print(f'Sum of invalid IDs: {sum}')

    # Problem 2
    file_path = Path(__file__).parent / 'data' / 'example2.txt'
    id_list = read_file(file_path)
    invalid_id_list = []
    for id_range in id_list:
        expanded_ids = expand_id(id_range)
        list = get_new_invalid_ids(expanded_ids)
        invalid_id_list.extend(list)
    sum = add_up_all_invalid_ids(invalid_id_list)
    print(f'Sum of invalid IDs: {sum}')