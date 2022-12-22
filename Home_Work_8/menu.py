import model

def list_menu():
    global input_id_employee
    global user_choice_second
    work_is_over = False

    while (not work_is_over):
        print('''
    Welcome!          
              
    Menu:
    
    1 View all data
    2 Surname search
    3 Search by position
    4 Add new employee
    5 Edit employee details
    6 Delete employee record
    7 Exiting the database''')
        
        user_choice_one = int(input('\nPlease enter option number: '))
        if (user_choice_one == 7):
            work_is_over = True
            print('Shutdown... Done.\nGood bye!')
            print()
        elif (user_choice_one == 1):  # показать всю базу сотрудников
            model.show_all_data()
        elif (user_choice_one == 2):  # поиск данных по фамилии сотрудника
            input_search_surname = input(
                'Please enter the surname of the employee: ')
            model.search_surname(input_search_surname)
            model.search()
        elif (user_choice_one == 3):
            input_function_employee = input(
                'Please enter the position of the employee: ')
            model.function_employ(input_function_employee)
            model.search_func()
        elif (user_choice_one == 4):  # добавить нового сотрудника
            model.add_new_employee()
        elif (user_choice_one == 5):  # изменить данные сотрудника по номеру id
            input_id_employee = int(input('Please enter employee ID: '))
            model.setSelected(input_id_employee)
            print('''
    Please select an option to edit:
    
    1 Surname
    2 Name
    3 Phone number
    4 Position''')
            user_choice_second = int(input('\nPlease enter option number: '))
            model.second_select(user_choice_second)
            input_update = input('Please enter new data: ')
            model.update_data(input_update)
            model.change_data()
        elif (user_choice_one == 6):
            input_id_employee = int(input('Please enter employee ID:'))
            model.setSelected(input_id_employee)
            model.delete_line()


list_menu()
