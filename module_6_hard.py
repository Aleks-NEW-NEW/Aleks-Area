class Figure:

    sides_count = 0

    def __init__(self, color, sides):
        self.__color = [*color]
        self.__sides = [*sides]
        self.filled = True
        self.check_filled()
        self.__is_valid_sides(*sides)


    def check_filled(self):
        for i in self.__color:
            if (i > 255) or (i < 0):
                self.filled = False
                return False
            elif self.__color.count(255) == len(self.__color):
                self.filled = False
                return False
        else:
            return True


    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        tuple_1 = r, g, b
        for j in tuple_1:
            if isinstance(j, int):
                if 0 <= j <= 255:
                    pass
                else:
                    break
            else:
                break
        else:
            return True


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            self.__sides.clear()
            self.__sides.extend([1] * self.sides_count)
            return False
        for s in sides:
            if (isinstance(s, int)) and (s > 0):
                continue
            else:
                return False
        else:
            return True


    def get_sides(self):
        return self.__sides


    def __len__(self):
        per_ = sum(self.__sides)
        return per_


    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                self.__sides = [*new_sides]



class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self._Figure__sides[0] / (3.14 * 2)


    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self._Figure__sides[0] / (3.14 * 2)


    def get_square(self):
        square = 3.14 * self.__radius ** 2
        return square


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)


    def get_square(self):
        p = self.__len__() / 2
        a_b_c = self._Figure__sides[:]
        square = (p * (p - a_b_c[0]) * (p - a_b_c[1]) * (p - a_b_c[2])) ** (1/2)
        return square


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if 1 == len(sides):
            self._Figure__sides.clear()
            self._Figure__sides.extend([*sides] * self.sides_count)
        elif sides.count(self._Figure__sides[0]) != len(sides):
            self._Figure__sides.clear()
            self._Figure__sides.extend([1] * self.sides_count)


    def get_volume(self):
        volume = self._Figure__sides[0] ** 3
        return volume



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проврека периметра (куба):
print(len(cube1))

# Проврека попытки создания (куба) с неравными сторонами:
cube2 = Cube((0, 0, 0), 4, 3, 1, 2, 4, 55, 56, 56, 3, 8, 7, 12) # Передаем 12 сторон.
print(cube2.get_sides())

# Создадим труголинк белого цвета и проверим закрашен он или нет. Также посчитаем его периметр и площадь.
triangle1 = Triangle((255, 255, 255), 10, 8, 12)
print(triangle1.check_filled())
print(len(triangle1))
print(triangle1.get_square())

# Изменим длину круга, и проверим поменялся ли радиус круга.
print('Радиус до изменения:', round(circle1._Circle__radius, 2))
circle1.set_sides(30)
print('Радиус после изменения:', round(circle1._Circle__radius, 2))
