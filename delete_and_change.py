from logger import *

def delete_change():
    cmd2 = '-1'
    while cmd2 not in ('0'):
        cmd2 = input('Выберите контакт или нажмите 0, чтобы выйти: ')
        print()   
                  
        data_str = read_file().rstrip().split('\n\n')
        save_index = int(cmd2) - 1
        get_user_contact = data_str[save_index]
        print(get_user_contact)
        print()

        while cmd2 not in ('0'):
            print('1. Изменить \n'
                '2. Удалить \n'
                '0. Меню')
            cmd2 = input('Выберите действие: ')
                            
            if cmd2 in ('1'):
                change_contact = input_contact()

                with open('phonebook.txt', 'r', encoding='utf-8') as data:
                    old_data = data.read()
                                
                new_data = old_data.replace(get_user_contact,change_contact)

                with open ('phonebook.txt', 'w', encoding='utf-8') as data:
                    data.write(new_data)
                cmd2 = '0'

            elif cmd2 in ('2'):

                with open('phonebook.txt', 'r', encoding='utf-8') as data:
                    old_data = data.read()
                                
                new_data = old_data.replace(get_user_contact,'')

                with open ('phonebook.txt', 'w', encoding='utf-8') as data:
                    data.write(new_data)

                cmd2 = '0'