def valid_input(func, max_Number):
    func = func.isdigit()
    if func == True:
        if func > 0 and func <= max_Number:
            return True
        else:
            print('You entered the wrong menu option.')
    else:
        print('Please enter a number for menu options.')
