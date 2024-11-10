def all_variants(text):

    i1 = 0
    i2 = 1
    s = 1

    while True:
        yield text[i1:i2]
        if len(text[i1:i2]) == len(text):
            break
        i1 += 1
        i2 += 1
        if i2 > len(text):
            i1 = 0
            i2 = 1 + s
            s += 1


a = all_variants("abc")
for i in a:
    print(i)

print()
b = all_variants("abcd")
for i in b:
    print(i)

print()
d = all_variants("abcdf")
for i in d:
    print(i)
