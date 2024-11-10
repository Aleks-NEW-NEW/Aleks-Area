def is_prime(func):
    def wrapper(n1, n2, n3):
        num = func(n1, n2, n3)
        if num in [0, 1]:
            return num
        for i in range(2, num + 1):
            if (num % i == 0) and num != i:
                print('Составное')
                break
        else:
            print('Простое')
        return num

    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    sum_numbers = sum((n1, n2, n3))
    return sum_numbers


result = sum_three(2, 3, 6)
print(result)
