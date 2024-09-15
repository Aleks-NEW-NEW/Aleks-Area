def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    tuple_1 = ('.com', '.ru', '.net')
    domain_r = []
    domain_s = []
    for i in tuple_1:
        if recipient.endswith(i):
            domain_r.append(i)
        if sender.endswith(i):
            domain_s.append(i)
    if (len(domain_r) == 0) or (len(domain_s) == 0):
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
