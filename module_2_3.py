my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index__my_list = 0

while True:
    if index__my_list == len(my_list):
        break
    elif my_list[index__my_list] == 0:
        index__my_list = index__my_list + 1
        continue
    elif my_list[index__my_list] > 0:
        print(my_list[index__my_list])
        index__my_list = index__my_list + 1
    else:
        break