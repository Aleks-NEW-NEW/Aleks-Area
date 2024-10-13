class Animal:

    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:

    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    alive = True
    fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Mammal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Mammal.alive = False


class Predator(Animal):
    alive = True
    fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Predator.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Predator.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.



#______Version 2________________________________________________________________________________
print('\n____________________Version 2_________________________')

class Animal_2:

    def __init__(self, name_2):
        self.name_2 = name_2
        self.alive_2 = True
        self.fed_2 = False

    def eat(self, food_2):
        if food_2.edible_2:
            print(f'{self.name_2} съел {food_2.name_2}')
            self.fed_2 = True
        else:
            print(f'{self.name_2} не стал есть {food_2.name_2}')
            self.alive_2 = False


class Plant_2:

    edible_2 = False

    def __init__(self, name_2):
        self.name_2 = name_2


class Mammal_2(Animal_2):
    pass

class Predator_2(Animal_2):
    pass

class Flower_2(Plant_2):
    pass

class Fruit_2(Plant_2):
    edible_2 = True


a3 = Predator_2('Волк с Уолл-Стрит')
a4 = Mammal_2('Хатико')
p3 = Flower_2('Цветик семицветик')
p4 = Fruit_2('Заводной апельсин')

print(a3.name_2)
print(p3.name_2)

print(a3.alive_2)
print(a4.fed_2)
a3.eat(p3)
a4.eat(p4)
print(a3.alive_2)
print(a4.fed_2)
