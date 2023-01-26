



  табличка. через библиотеку tkinter




import tkinter import*
import tkinter import ttk


root = Tk()
root.title( титульный листочек )
root.geometry(700x200)

#определение данных для отображения
contact = [( "ivanov" 21321564 "ivan")]

#столбцы
columns = ("фамилия", "телефон", "фамилия" )

tree = tkk.Treeview(columns = columns, show = "head")
tree.pack(fill=Both , expand = 1)


#определение заголовков
tree.heading("name", text = "Имя")
tree.heading("name", text = "телефон")
tree.heading("name", text = "фамилия")

#добавление данных
for contact in contacts:
    tree.insert("",END, valuves = contact)
root.mainloop





Export_contact.txt ( контакты в формате txt)



ivanov Ivan 1234566987 Slesar
Viktor Victorov 123456789 Tokar
San Sanich 321654785 Mechanic
Grigorii Rudenko 6565656565 Motorman
Tepan Semenovich 452454 Gidravlist





add_contact.py( модуль добавления контактов )

import json
import contriller


def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    contriller.user_choice()


def add_to_json():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    json_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nУспешно добавлен в список контактов!\n')
    contriller.user_choice()







change_phone_number.py ( блок изменения телефонного номера )



import json
import contriller


path_to_db = 'db.json'


def change_phone_number():  
    name = input('Введите имя или фамилию контакта, номер телефона которого нужно изменить:  ')
   
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый телефон: ')
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер успешно изменён!\n')
    contriller.user_choice()





change_surname.py ( блок изменения имени )


import json
import contriller

path_to_db = 'db.json'


def change_surname():
    name = input(
        'Введите имя или фамилию контакта, фамилию которого необходимо изменить:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Surname'] = input('Новая фамилия: ')
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nФамилия успешно изменена!\n')
    contriller.user_choice()




contriller.py 


import add_contact as ac
import user_interface as ui
import change_phone_number as cpn
import change_surname as cs
import delete_contact as dc
import view_all_contacts as vac
import export_in_file as eif


def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        ac.create_json()
    elif choice_num == 1:
        ac.add_to_json()
    elif choice_num == 2:
        cpn.change_phone_number()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        dc.delete_contact()
    elif choice_num == 5:
        vac.view_all_contacts()
    elif choice_num == 6:
        eif.export_txt()
    elif choice_num == 7:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()












Db.json



[
    {
        "Name": "EIvan",
        "Surname": "Ivan",
        "Phone number": "",
        "Comment": ""
    }
    
]


delete_contact.py

import json
import contriller


path_to_db = 'db.json'


def delete_contact():
    name = input('Введите имя или фамилию контакта, который необходимо удалить:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nКонтакт успешно изменена удалён!\n')
    contriller.user_choice()



export_in_file.py

import json
import contriller
path_to_db = 'db.json'


def export_txt():
    # name = input('Введите имя или фамилию контакта, для экспорта в файл:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
           # if name == data[i]['Name'] or name == data[i]['Surname']:
                with open('Export_contact.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                        data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно добавлен в файл!\n')
    contriller.user_choice()




main

import contriller
import user_interface as ui

ui.start()
contriller.user_choice()



interface user

import chek
from export_in_file import export_txt


def start():
    greetings = 'Привет! Это твоя телефонная книга. Давай расскажу что я умею\nМы можем создать новый контакт, найти его, изменить или удалить,\nа также показать все контакты.'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'ВЫбрать из списка нужное действие:'
    new_book = '0. Создать новую книгу или очистить существующую'
    new_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_surname = '3. Изменить фамилию'
    delete_contact = '4. Удалить контакт'
    view_all_contact = '5. Показать все контакты'
    export_to_file = '6. Экспортировать контакты в файл'
    to_exit = '7. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n{view_all_contact}\n{export_to_file}\n{to_exit}')
    return chek.digit_check()






view_all_contacts.py


import json
import contriller


path_to_db = 'db.json'


def view_all_contacts():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    contriller.user_choice()




