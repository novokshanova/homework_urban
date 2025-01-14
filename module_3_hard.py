def calculate_structure_sum(data_structure, *args):
    total_sum = 0
    for item in data_structure:
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple, dict, set)):
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для вложенных структур
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int, float)):
                    total_sum += key
                elif isinstance(key, str):
                    total_sum += len(key)
                if isinstance(value, (int, float)):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                elif isinstance(value, (list, tuple, dict, set)):
                    total_sum += calculate_structure_sum(value)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Output: 99
