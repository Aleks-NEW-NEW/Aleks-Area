def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    number_of_str = 1
    strings_positions = dict()
    for s in strings:
        strings_positions[(number_of_str, file.tell())] = s
        file.write(s + '\n')
        number_of_str += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
