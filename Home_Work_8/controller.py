from push_data import *
from read_data import *
from print_data import *
from search_data import *


def start():
    print('''Menu for working with the database of school students:\n\
    1 - Display all students information.\n\
    2 - Add new student.\n\
    3 - Find a student.\n\
    4 - Exit.''')
    ch = input("Please enter option number: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Enter data to search a student: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Student not found. Please search again.")
            start()
        elif ch == '4':
            print("Exiting the program ... Done")
            break
        else:
            print(
                "You entered the wrong menu option. Please enter a number for menu options.")
            start()
