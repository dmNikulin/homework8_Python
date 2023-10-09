def name_data():
    return input('Введите имя: ')

def surname_data():
    return input('Введите фамилию: ')

def patronymic_data():
    return input('Введите отчество: ')

def phone_number_data():
    return input('Введите номер: ')

def address_data():
    return input('Введите адресс: ')

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone = phone_number_data()
    address = address_data()

    return f'{name} {surname} {patronymic} \n {phone} \n {address}'

def add_contact():
    contact = input_contact()
    with open('phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(contact + '\n \n')

def read_file():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        return data.read()
    
def print_contacts():
    
    data = read_file()
    print()
    print(data)

def search_contacts():
    print('Меню: \n'
            '1. По имени \n'
            '2. По фамилии \n'
            '3. По отчеству \n'
            '4. По телефону \n'
            '5. По телефону \n')
    
    choice = input('Выберите вариант для поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')

    data_str = read_file().rstrip()

    if search not in data_str:
        print('Такого контакта не существует!')
    else:
        print([data_str])
        data_lst = data_str.split('\n\n')
        print(data_lst)

        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n',' ').split()
            if search in contact_lst[i_choice]:
                print(contact_str)
                print(contact_lst)
                print()

def user_interface():

    with open('phonebook.txt', 'a', encoding = 'utf-8'):         # Создаем файл, если его нет
        pass

    cmd = None

    while cmd != '4':

        print('Меню: \n'
            '1. Запись контакта \n'
            '2. Вывести контакты на экран \n'
            '3. Поиск контакта \n'
            '4. Выход')
        
        cmd = input('Выберите действие: ')

        while cmd not in ('1', '2', '3', '4'):
            print('Некорреутный ввод: ')
            cmd = input('Выберите действие: ')

        match cmd:
            case '1':
                add_contact()

            case '2':
                print_contacts()

            case '3':
                search_contacts()
            
            case '4':
                print('До свидания!')

user_interface()