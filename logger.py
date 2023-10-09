from data_create import *


def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'


def add_contact():
    contact = input_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')


def read_file():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()


def print_contacts():
    data_str = read_file().rstrip().split('\n\n')

    number_position = 1

    for i in range(len(data_str)):
        print(f'{number_position}) {data_str[i]}')
        print()
        number_position += 1



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
    print()
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Такого нету')
    else:
        #print([data_str])
        data_lst = data_str.split('\n\n')
        #print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                # print(contact_lst)
                print(contact_str)
                print()
