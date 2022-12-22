def read_data():
    list_name = []
    with open('students.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            list_name.append(temp)
        print(list_name)
    list_address = []
    with open('address.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            list_address.append(temp)
        print(list_address)

    list_class = []
    with open('class.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            list_class.append(temp)
        print(list_class)

    my_list = []
    for i in range(len(list_name)):
        my_list.append([list_name[i][0], list_name[i][1], list_name[i][2], list_name[i][3], list_name[i][4],
                    list_class[i][1], list_class[i][2],
                    list_address[i][1], list_address[i][2], list_address[i][3], list_address[i][4], list_address[i][5]])
    return my_list
