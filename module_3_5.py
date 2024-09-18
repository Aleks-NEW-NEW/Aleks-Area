def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        return 1
    elif len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
result_2 = get_multiplied_digits(402030)
print(result_2)