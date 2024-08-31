my_dict = {'Kosti': 2000, 'Alena': 1999, 'Misha': 1987, 'Katy': 1995}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alena'], '\n' + 'Not existing value:', my_dict.get('Aleks'))
my_dict.update({'Aleks': 1991, 'Dima': 1993})
del_1 = my_dict.pop('Kosti')
print('Deleted value:', del_1)
print('Modified dictionary:', my_dict)

print()

my_set = {1, 'Cat', (0, 'Dog'), True, 'Cat', 1, (0, 'Dog'), True}
print('Set:', my_set)
my_set.add(45.6)
my_set.add('Aleks')
my_set.discard((0, 'Dog'))
print(f'Modified set: {my_set}')