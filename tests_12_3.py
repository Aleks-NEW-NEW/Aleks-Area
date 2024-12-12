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

                if participant.distance >= self.full_distance:
                    if participant.speed < max(i.speed for i in self.participants):
                        continue

                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

                participant.run()

        return finishers


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('Bob')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Anna')
        for j in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Snake')
        runner_4 = Runner('Snail')
        for k in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    @unittest.skipIf(is_frozen, 'Метод "setUp" заморожен')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
        # print('__' * 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        self.tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_1.start()).items()}
        self.all_results['test_1'] = update_dict
        self.assertTrue(self.all_results['test_1'][max(self.all_results['test_1'].keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        self.tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_2.start()).items()}
        self.all_results['test_2'] = update_dict
        self.assertTrue(self.all_results['test_2'][max(self.all_results['test_2'].keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        self.tournament_3 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict = {k: v.name for k, v in (self.tournament_3.start()).items()}
        self.all_results['test_3'] = update_dict
        self.assertTrue(self.all_results['test_3'][max(self.all_results['test_3'].keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed(self):
        self.tournament_3 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        update_dict_with_speed = {v.speed: v.name for k, v in (self.tournament_3.start()).items()}

        self.assertTrue(self.all_results['test_3'][min(self.all_results['test_3'].keys())] ==
                        update_dict_with_speed[max(update_dict_with_speed.keys())],
                        f'{self.all_results['test_3'][min(self.all_results['test_3'].keys())]} != '
                        f'{update_dict_with_speed[max(update_dict_with_speed.keys())]}')


if __name__ == '__main__':
    unittest.main()
