numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for k in numbers[1:]:
        if (i % k == 0) and (i != k):
            is_prime = False
            break
        elif (i > k) and (i % k != 0):
            continue
        else:
            break
    if is_prime == False:
        not_primes.append(i)
    else:
        primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)

print()

#___Version 2________________________________________________________
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = set(numbers)
numbers.remove(1)
numbers = list(numbers)
numbers.sort()

primes = []
not_primes = []

for i in numbers:
    for k in numbers:
        if (i % k == 0) and (i != k):
            not_primes.append(i)
            break
        elif i > k:
            continue
        else:
            primes.append(i)
            break

print('Primes:', primes)
print('Not Primes:', not_primes)