my_string = str(input('Ввод текста: '))

# Вывод на экран количество символов без учёта пробела.
print('Кол. символов:', my_string.replace(' ', '').count('') - 1)

print(my_string.upper())
print(my_string.lower())
my_string = my_string.replace(' ', '')
print(my_string[0])
print(my_string[-1])