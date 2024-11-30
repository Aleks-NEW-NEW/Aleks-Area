import time
import threading
import queue
from random import randint



class Table:

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        self.free_tables = len(self.tables)
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.start()
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    self.free_tables -= 1
                    break
            else:
                self.queue.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        while (not self.queue.empty()) or (self.free_tables < len(self.tables)):

            for t in self.tables:
                if t.guest is not None:
                    if not t.guest.is_alive():
                        print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {t.number} свободен')
                        t.guest = None
                        self.free_tables += 1

            if (not self.queue.empty()) and (self.free_tables > 0):
                for t in self.tables:
                    if t.guest is None:
                        t.guest = self.queue.get()
                        print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                        t.guest.start()
                        self.free_tables -= 1
                        break



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
