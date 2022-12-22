from write_data import count_data


def input_data():
    dict = dict()
    Id = count_data("students.csv")
    dict["id"] = Id
    dict["surname"] = input('Please enter surname: ')
    dict["name"] = input('Please enter name: ')
    dict["class"] = input('Please enter class: ')
    dict["status"] = input('Student achievement level: ')
    dict["row"] = input('Please enter row number: ')
    dict["col"] = input('Please enter desk number: ')
    dict["city"] = input('Please enter city name: ')
    dict["street"] = input('Please enter a street name: ')
    dict["house"] = input('Please enter house number: ')
    dict["apartment"] = input('Please enter apartment number: ')
    dict["other"] = input('Please enter additional information: ')
    return dict
