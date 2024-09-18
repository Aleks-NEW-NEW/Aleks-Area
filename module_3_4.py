def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.upper()
    other_words = [*other_words]
    for i in other_words:
        if (root_word in i.upper()) or (i.upper() in root_word):
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
