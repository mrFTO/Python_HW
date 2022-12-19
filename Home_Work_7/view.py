def menu():
    print('''Menu:
    1 Add new contact
    2 Edit contact
    3 Delete contact
    4 View contact
    5 View all contacts ''')
    user_input = input('Please enter option number: ')
    return user_input


def contact(text):
    return input(text)


def add_user():
    user_contact = []
    id_add = contact('id ')
    user_contact.append(id_add)
    f_name = contact('Name: ')
    user_contact.append(f_name)
    l_name = contact('Surname: ')
    user_contact.append(l_name)
    number_phone = contact('Phone number: ')
    user_contact.append(number_phone)
    other = contact('Additional Information: ')
    user_contact.append(other)
    return user_contact
