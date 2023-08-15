def Display(phone_data, page_number, page_size):
    print(f'Количество контактов: {len(phone_data)}')

    # page_number = int(input('номер страницы: '))
    # page_size = int(input('количество записей на странице: '))

    if (len(phone_data) > page_number) or ((len(phone_data) == page_number) and page_size == 1):
        if len(phone_data) % page_size == 0:
            print(f'Всего страниц: {len(phone_data) // page_size}')
        else:
            print(f'Всего страниц: {len(phone_data) // page_size + 1}')
    else:
        print(f'на странице {page_number} пока нет записей')

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    page_records = phone_data[start_index:end_index]

    for record in page_records:

        print('-------------')
        print(f'Контакт №{phone_data.index(record) + 1}:')
        print(f"ФИО: {record['last_name']} {record['first_name']} {record['middle_name']}")
        print(f"Организация: {record['organization']}")
        print(f"Телефон(рабочий/личный): {record['work_phone']} / {record['personal_phone']}")
        print('-------------')


def Search(phone_data):
    contacts = {}
    result = []

    last_name = input("Введите фамилию (или нажмите Enter, если не нужно искать по этому параметру): ")
    first_name = input("Введите имя (или нажмите Enter, если не нужно искать по этому параметру): ")
    middle_name = input("Введите отчество (или нажмите Enter, если не нужно искать по этому параметру): ")
    organization = input("Введите название организации (или нажмите Enter, если не нужно искать по этому параметру): ")
    work_phone = input("Введите рабочий телефон (или нажмите Enter, если не нужно искать по этому параметру): ")
    personal_phone = input("Введите личный телефон (или нажмите Enter, если не нужно искать по этому параметру): ")

    for contact in phone_data:
        if (not last_name or contact["last_name"].lower() == last_name.lower()) and \
        (not first_name or contact["first_name"].lower() == first_name.lower()) and \
        (not middle_name or contact["middle_name"].lower() == middle_name.lower()) and \
        (not organization or contact["organization"].lower() == organization.lower()) and \
        (not work_phone or contact["work_phone"].lower() == work_phone.lower()) and \
        (not personal_phone or contact["personal_phone"].lower() == personal_phone.lower()):
            contacts[f'Контакт №{phone_data.index(contact) + 1}'] = contact
            # print(f"ФИО: {contact['last_name']} {contact['first_name']} {contact['middle_name']}")
            # print(f"Организация: {contact['organization']}")
            # print(f"Телефон(рабочий/личный): {contact['work_phone']} / {contact['personal_phone']}")
            result.append(contacts)

