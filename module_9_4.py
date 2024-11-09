#_______________Lambda-функция_________________
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


#_______________Замыкание_________________
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(list((str(i) + '\n' for i in data_set)))
            # for i in data_set:
            #     file.write(str(i) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


#_______________Метод __call__:_________________
from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = [*words]

    def __call__(self):
        word = choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
