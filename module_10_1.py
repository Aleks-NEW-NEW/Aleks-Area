import time
import datetime
import threading


def write_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.datetime.now()
print(f'Работа потоков {end - start}')


start = datetime.datetime.now()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
list_threads = [thread_1, thread_2, thread_3, thread_4]
for k in list_threads:
    k.start()
for j in list_threads:
    j.join()
end = datetime.datetime.now()
print(f'Работа потоков {end - start}')
