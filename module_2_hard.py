number_on_stone_1 = int(input('Введите число 1-ого камня: '))

result = list()
set_numbers = list()

for l in range(number_on_stone_1):
    set_numbers.append(l+1)

set_numbers.pop(-1)

for i in set_numbers:
    for k in set_numbers[set_numbers.index(i)+1:]:
        if number_on_stone_1 % (i + k) == 0:
            result.append([i, k])

print('Пароль для 2-ого камня:',
      str(result).replace(', ', '').replace('[', '').replace(']', ''))

print()
print('pair_result:', result)