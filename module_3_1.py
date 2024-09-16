calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    string = str(string)
    tuple_1 = len(string), string.upper(), string.lower()
    count_calls()
    return tuple_1

def is_contains(string, list_to_search):
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    count_calls()
    return True if string in list_to_search else False


print(string_info('SpongeBob'))
print(string_info('Patrick'))
print(is_contains('SPONGEBOB', ['Squidward', 'Patrick', 'SpongeBob']))
print(is_contains('MrCrabs', ['Squidward', 'Patrick', 'SpongeBob']))
print(calls)
