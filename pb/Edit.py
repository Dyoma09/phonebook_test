from .utils import save_phonebook
def add_contact(phone_data):
	contact = {}

	contact['last_name'] = input('введите фимилию: ')
	contact['first_name'] = input('введите имя: ')
	contact['middle_name'] = input('введите отчество: ')
	contact['organization'] = input('введите название организации: ')
	contact['work_phone'] = input('введите номер рабочего телефона: ')
	contact['personal_phone'] = input('введите номер личного телефона: ')
	# contact_id = len(phone_data) + 1
	# contact_list[f'contact_{contact_id}'] = contact

	phone_data.append(contact)

	save_phonebook(phone_data)


def edit_contact(phone_data, num):

	num = int(input('введите номер контакта, который хотите изменить:'))
	edit = phone_data[num - 1]
	print('------')
	print(f'''Контакт №{num}:
{edit['last_name']} {edit['first_name']}''')
	print('------')

	command = input('''введите команду для редактирования:
	N - имени;
	F - фамилии;
	M - отчества; 
	O - названия организации;
	W - рабочего телефона;
	P - личного телефона;
	A - контакта целиком;
	''').upper()
	if command == 'F':
		print(edit["last_name"])
		edit["last_name"] = input("Введите фамилию: ").title()
		print(f'изменено на |-> {edit["last_name"]}')
	elif command == 'N':
		print(edit["first_name"])
		edit["first_name"] = input("Введите имя: ").title()
		print(f'изменено на |-> {edit["first_name"]}')
	elif command == 'M':
		print(edit["middle_name"])
		edit["middle_name"] = input("Введите отчество: ").title()
		print(f'изменено на |-> {edit["middle_name"]}')
	elif command == 'O':
		print(edit["organization"])
		edit["organization"] = input("Введите название организации: ")
		print(f'изменено на |-> {edit["organization"]}')
	elif command == 'W':
		print(edit["work_phone"])
		edit["work_phone"] = input("Введите рабочий телефон: ")
		print(f'изменено на |-> {edit["work_phone"]}')
	elif command == 'P':
		print(edit["personal_phone"])
		edit["personal_phone"] = input("Введите личный телефон: ")
		print(edit["personal_phone"])
	elif command == 'A':
		edit["last_name"] = input("Введите фамилию: ").title()
		edit["first_name"] = input("Введите имя: ").title()
		edit["middle_name"] = input("Введите отчество: ").title()
		edit["organization"] = input("Введите название организации: ")
		edit["work_phone"] = input("Введите рабочий телефон: ")
		edit["personal_phone"] = input("Введите личный телефон: ")
	else:
		print('Редактирование отменено')

	save_phonebook(phone_data)


