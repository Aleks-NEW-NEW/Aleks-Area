import inspect


def introspection_info(obj):

    string_info = f"""Объект исследования: {obj}
Тип объекта: {type(obj)}
Атрибуты объекта: {dir(obj)}
Методы объекта: {[i for i in dir(obj) if callable(getattr(obj, i))]}
Модуль: {str(inspect.getmodule(obj, 'module_11_3.py')).split()[1]}
ID объекта: {id(obj)}
Объект является числом: {'Да' if isinstance(obj, (int, float)) else 'Нет'}
Документация про объект: {obj.__doc__}"""

    return string_info


number_info = introspection_info(42)
print(number_info)
print()


class Car:

    """Класс 'Car' предназначен для
закрепления знаний об интроспекции.
Класс обладает методом, который может вывести
в консоль максимальную скорость объекта
этого класса в зависимости от мощности.
    """

    def __init__(self, power, color):
        self.power = power
        self.color = color

    def max_speed(self):
        print(f'{self.power * 1.3:.2f} км\ч')


car_1 = Car(57, 'Красный')

print(introspection_info(car_1))
