import view
import function_s
import validation


def button_click():
    file_work = "output.csv"
    menu = view.menu()
    x = validation.valid_input(menu, 5)
    if x == True:
        if menu == "1":
            user_contact = view.add_user()
            function_s.add(user_contact, file_work)
        elif menu == "2":
            id_user = view.contact('Please enter ID: ')
            function_s.change(id_user, file_work)
        elif menu == "3":
            id_user = view.contact('Please enter ID: ')
            x = validation.valid_input(id_user, 2)
            if x == True:
                function_s.view_id(id_user, file_work)
                input_user = view.contact(
                    'This line will be deleted for confirmation press 1 or any other character for refusal.')
                if input_user == "1":
                    print('Your line has been permanently deleted.')
                    function_s.dell(id_user, file_work)
                else:
                    button_click()
        elif menu == "4":
            function_s.view_id(view.contact('Please enter ID: '), file_work)
        elif menu == "5":
            function_s.view_all(file_work)
    else:
        button_click()
