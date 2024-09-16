#___1-st p. of the task_________________________________________
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(False, None, 1.15)
print_params(4, 'string')
print_params()
# check
print()
print_params(b = 25)
print_params(c = [1,2,3])
print()

#___2-nd p. of the task_________________________________________
values_list = [13.8, 'Marry', False]
values_dict = {'a': 'Bob', 'b': 45, 'c': ()}

print_params(*values_list)
print_params(**values_dict)
print()

#___3-rd p. of the task_________________________________________
values_list_2 = ['a', 95]
print_params(*values_list_2, 42)
