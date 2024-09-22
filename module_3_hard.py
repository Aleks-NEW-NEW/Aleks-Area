data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


sum_all = 0

def calculate_structure_sum(data_structure_):
    global sum_all
    for i in data_structure_:
        if isinstance(i, int):
            sum_all = sum_all + i
            continue
        elif isinstance(i, str):
            sum_all = sum_all + len(i)
            continue
        elif isinstance(i, dict):
            calculate_structure_sum(i.items())
            continue
        elif len(i) == 0:
            continue
        calculate_structure_sum(i)
    return sum_all


result = calculate_structure_sum(data_structure)
print(result)
