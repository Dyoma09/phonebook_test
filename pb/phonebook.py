import json

from .utils import phonebook, save_phonebook
from .Edit import add_contact, edit_contact
from .Display import Display, Search

def load_phonebook():
	with open(phonebook, 'r', encoding='utf-8') as f:
		data = f.read()
		phone_data = json.loads(data)

		return phone_data
        
def main_menu():
    """
    Функция главного меню программы.
    """
    phone_data = load_phonebook()

    while True:
        print("1. Вывести записи справочника")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            page_number = int(input("Введите номер страницы: "))
            page_size = int(input("Введите размер страницы: "))
            Display(phone_data, page_number, page_size)
        elif choice == "2":
            add_contact(phone_data)
        elif choice == "3":
            num = int(input("Введите идентификатор записи: "))
            edit_contact(phone_data, num)
        elif choice == "4":
            result = search_contacts(phone_data)
            if result:
                print("Найденные записи:")
                for contact in result:
                    print(contact)
            else:
                print("Записи с указанными параметрами не найдены.")
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    print("До свидания!")

if __name__ == "__main__":
    main_menu()