import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}, {self.password}, {self.age}'


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return f'{self.title}, {self.duration}, {self.adult_mode}, {self.time_now}'


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if (nickname == i.nickname) and (hash(password) == i.password):
                self.current_user = nickname

    def register(self, nickname, password, age):
        flag = True
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже существует')
                flag = False
                break
        if flag:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for k in videos:
            for j in self.videos:
                if j.title.strip() == k.title.strip():
                    break
            else:
                self.videos.append(k)

    def get_videos(self, title):
        for_print = []
        for j in self.videos:
            if title.lower() in j.title.lower():
                for_print.append(j.title)
        return for_print

    def watch_video(self, title):
        flag = False
        video = None
        for j in self.videos:
            if j.title == title:
                video = j
                if isinstance(self.current_user, str):
                    if j.adult_mode:
                       for i in self.users:
                           if i.nickname == self.current_user:
                               if i.age >= 18:
                                   flag = True
                                   break
                               else:
                                   return print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        flag = True
                else:
                    return print('Войдите в аккаунт, чтобы смотреть видео')
                break
        if flag:
            while video.duration > video.time_now:
                video.time_now += 1
                time.sleep(1)
                print(video.time_now, end=' ')
            print('Конец видео')
            video.time_now = 0



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
