class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = dict()
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                str_1 = file.read().lower()
                str_1 = str_1.replace(' - ', ' ')
                list_symbol = [',', '.', '=', '!', '?', ';', ':']
                for sym in list_symbol:
                    str_1 = str_1.replace(sym, '')
                all_words[f] = str_1.split()
        return all_words


    # get_all_words. Version 2
    # def get_all_words(self):
    #     all_words = dict()
    #     for f in self.file_names:
    #         with open(f, encoding='utf-8') as file:
    #             words_on_string = str()
    #             for s in file:
    #                 s.lower()
    #                 s = s.replace(' - ', ' ')
    #                 list_symbol = [',', '.', '=', '!', '?', ';', ':']
    #                 for sym in list_symbol:
    #                     s = s.replace(sym, '')
    #                 words_on_string += s
    #             all_words[f] = words_on_string.split()
    #     return all_words


    def find(self, word):
        dict_1 = dict()
        for k, v in self.get_all_words().items():
            if word.lower() not in v:
                dict_1[k] = None
                continue
            dict_1[k] = v.index(word.lower()) + 1
        return dict_1


    def count(self, word):
        dict_1 = dict()
        for k, v in self.get_all_words().items():
            dict_1[k] = v.count(word.lower())
        return dict_1



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
