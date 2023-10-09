def name_data():
    return input('Введите имя: ')


def surname_data():
    return input('Введите фамилию: ')


def patronymic_data():
    return input('Введите отчество: ')


def phone_number_data():
    return input('Введите номер телефона: ')


def address_data():
    return input('Введите адрес: ')

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'


def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')


def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()


def print_contacts():
    data = read_file()
    print()
    print(data)


def search_contact():
    print('Варианты поиска:\n'
          '1. По имени\n'
          '2. По фамилии\n'
          '3. По отчеству\n'
          '4. По номеру телефона\n'
          '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Такого нету')
    else:
        # print([data_str])
        data_lst = data_str.split('\n\n')
        # print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                # print(contact_lst)
                print(contact_str)
                print()

def user_interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):  # создаем файл если его нет
        pass
    cmd = None
    while cmd != '4':
        print('Меню:\n'
              '1. Запись контакта\n'
              '2. Вывести данные на экран\n'
              '3. Поиск контакта\n'
              '4. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                print('До свидания))')

user_interface()
