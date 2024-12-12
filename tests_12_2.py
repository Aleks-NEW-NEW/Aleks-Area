import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
        print('__' * 50)

    def test_1(self):
        self.tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_1.start()).items()}
        self.all_results['test_1'] = update_dict
        self.assertTrue(self.all_results['test_1'][max(self.all_results['test_1'].keys())] == 'Ник')

    def test_2(self):
        self.tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_2.start()).items()}
        self.all_results['test_2'] = update_dict
        self.assertTrue(self.all_results['test_2'][max(self.all_results['test_2'].keys())] == 'Ник')

    def test_3(self):
        self.tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_3.start()).items()}
        self.all_results['test_3'] = update_dict
        self.assertTrue(self.all_results['test_3'][max(self.all_results['test_3'].keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()


#   Если поменять порядок передачи участников забега, например Усэйна и Андрея поменять местами, то Андрей
# прибежит первый. Хотя его скорость меньше скорости Усэйна. Повторно проведем тест.
class TournamentTest_2(TournamentTest):

    # Переопределим 'test_3'. Меняем местами участников. Видим что Андрей прибежал первый.
    def test_3(self):
        self.tournament_3 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_3.start()).items()}
        self.all_results['test_3'] = update_dict
        self.assertTrue(self.all_results['test_3'][max(self.all_results['test_3'].keys())] == 'Ник')

    # Дополнительный тест на скорость участников.
    def test_speed(self):
        self.tournament_3 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict_with_speed = {v.speed: v.name for k, v in (self.tournament_3.start()).items()}

        # Сравниваю имена участников, того кто занял первое место с тем у кого максимальная скорость.
        # Так же в сообщении(2-ой параметр 'msg:') метода 'assertTrue' принтую не совпадение имен, если
        #   если логическое выражение (1-ый параметр метода) вернуло 'False'.
        self.assertTrue(self.all_results['test_3'][min(self.all_results['test_3'].keys())] ==
                        update_dict_with_speed[max(update_dict_with_speed.keys())],
                        f'{self.all_results['test_3'][min(self.all_results['test_3'].keys())]} != '
                        f'{update_dict_with_speed[max(update_dict_with_speed.keys())]}')


if __name__ == '__main__':
    unittest.main()


#   Напишем новый класс 'Tournament_2' наследуясь от старого.
# В котором переопределим метод 'start'.
class Tournament_2(Tournament):

    def __init__(self, distance, *participants):
        super().__init__(distance, *participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:

                # Если участник забега пробежал полную дистанцию, то проверяем его скорость.
                # Если его скорость не максимальная, то он ждет пока пробежит участник с максимальной скорость.
                if participant.distance >= self.full_distance:
                    if participant.speed < max(i.speed for i in self.participants):
                        continue

                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

                #   Сместим вызов метода 'run()' для участника вниз цикла,
                participant.run()

        return finishers


# Проводим повторно тест.
class TournamentTest_3(TournamentTest_2):

    #   Так же переопределяю метод, т.к. изменился класс 'Tournament'.
    # Меняю класс 'Tournament' на 'Tournament_2'.
    def test_3(self):
        self.tournament_3 = Tournament_2(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_3.start()).items()}
        self.all_results['test_3'] = update_dict
        self.assertTrue(self.all_results['test_3'][max(self.all_results['test_3'].keys())] == 'Ник')

    # Тоже самое, что и с предыдущим методом.
    def test_speed(self):
        self.tournament_3 = Tournament_2(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict_with_speed = {v.speed: v.name for k, v in (self.tournament_3.start()).items()}

        self.assertTrue(self.all_results['test_3'][min(self.all_results['test_3'].keys())] ==
                        update_dict_with_speed[max(update_dict_with_speed.keys())],
                        f'{self.all_results['test_3'][min(self.all_results['test_3'].keys())]} != '
                        f'{update_dict_with_speed[max(update_dict_with_speed.keys())]}')


# Создам 'чистый' класс 'Tournament_3' со всеми изменениями для повторной проверки тестом.
class Tournament_3:

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:

                if participant.distance >= self.full_distance:
                    if participant.speed < max(i.speed for i in self.participants):
                        continue

                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

                participant.run()

        return finishers


# Так же создам новый класс тест 'TournamentTest_4' со всеми изменениями.
class TournamentTest_4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
        print('__' * 50)

    def test_1(self):
        self.tournament_1 = Tournament_3(90, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_1.start()).items()}
        self.all_results['test_1'] = update_dict
        self.assertTrue(self.all_results['test_1'][max(self.all_results['test_1'].keys())] == 'Ник')

    def test_2(self):
        self.tournament_2 = Tournament_3(90, self.runner_2, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_2.start()).items()}
        self.all_results['test_2'] = update_dict
        self.assertTrue(self.all_results['test_2'][max(self.all_results['test_2'].keys())] == 'Ник')

    def test_3(self):
        self.tournament_3 = Tournament_3(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_3.start()).items()}
        self.all_results['test_3'] = update_dict
        self.assertTrue(self.all_results['test_3'][max(self.all_results['test_3'].keys())] == 'Ник')

    def test_speed(self):
        self.tournament_3 = Tournament_3(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict_with_speed = {v.speed: v.name for k, v in (self.tournament_3.start()).items()}

        self.assertTrue(self.all_results['test_3'][min(self.all_results['test_3'].keys())] ==
                        update_dict_with_speed[max(update_dict_with_speed.keys())],
                        f'{self.all_results['test_3'][min(self.all_results['test_3'].keys())]} != '
                        f'{update_dict_with_speed[max(update_dict_with_speed.keys())]}')


# Проводим тест.
if __name__ == '__main__':
    unittest.main()
