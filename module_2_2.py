first = int(input('1-st: '))
second = int(input('2-nd: '))
third = int(input('3-rd: '))

if first == second == third:
    print(3)
elif (second == third) or (first == second) or (first == third):
    print(2)
else:
    print(0)

# __Version 2______________________________________________________
if first == second == third:
    print(3)
elif first != second != third != first:
    print(0)
else:
    print(2)
