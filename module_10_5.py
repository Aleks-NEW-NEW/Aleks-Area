import multiprocessing
import datetime


def read_info(file_name):
    all_data = list()
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# start = datetime.datetime.now()
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
# end = datetime.datetime.now()
# print(f'{end - start} (линейный)')


if __name__ == '__main__':

    start = datetime.datetime.now()
    with multiprocessing.Pool(4) as p:
        p.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')
