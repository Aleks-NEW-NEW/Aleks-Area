# Task 1__________________________________________________________________
str_1 = 'abc'
int_1 = 1343
float_1 = 25.7
bool_1 = True
list_1 = [0, 'ss']
list_2 = [1, 'jj']

immutable_var = (str_1, int_1, float_1, bool_1, list_1)
print(immutable_var)

# Объект типа "кортеж" является не изменяемым типом данных.
# Попробуем изменить.
# immutable_var[0] = 'x'    # Питон выдаст ошибку "TypeError: 'tuple' object does not support item assignment"
# Аналогично для следующих 3 объектов кортежа, питон выдает ошибку.
# immutable_var[1] = 0
# immutable_var[2] = 65.1
# immutable_var[3] = False
# Но для четвертого объекта кортежа, который являеться изменяемым типом данных типа "список", операция по изменению
# сработает. Но при условии, что мы будем изменять объекты списка, а не сам объект типа список в кортеже, т.к.
# объект типа "кортеж" является не изменяемым типом данных.
immutable_var[4][0] = 'A'
print(immutable_var)
# immutable_var[4] = list_2  # Питон выдаст ту же самую оишбку: "TypeError: 'tuple' object does not support item assignment"
# Попробую изменить объекты переменых, которые я садал в самом начале программы.
# str_1[0] = 'k'             # Питон выдаст ошибку "TypeError: 'str' object does not support item assignment"
# int_1[0] = 9               # Питон выдаст ошибку
# float_1[0] = 30.4          # Питон выдаст ошибку
# bool_1[0] = False          # Питон выдаст ошибку
list_1[0] = 'xxx'
print(list_1)
# Делаю вывод, что объекты кортежа изменять нельзя, можно только изменять изменяемые объекты кортежа в нутри этих объектов.


# Task 2__________________________________________________________________
print()
mutable_list = ['Aleks', 118.43, True, (1, 3, 5, 'acfr')]
mutable_list[0] = mutable_list[0].upper()
mutable_list[1] = mutable_list[2]
mutable_list[2] = str(mutable_list[2])
mutable_list.extend(mutable_list[2])
mutable_list.remove('True')
mutable_list[2] = ((mutable_list[2]) + ("Double",)) * 2
print(mutable_list)