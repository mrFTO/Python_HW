def print_data(data, search=False):
    if len(data) > 0:
        print("id".center(5), "Surname".center(20), "Name".center(10), "Class".center(6), "Status".center(6),
              "Row".center(4), "Desk".center(6),
              "City".center(15), "Street".center(15), "House".center(6), "Apartment".center(4), "Addition".center(20))
        print("-"*70)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(5), item[1].center(20), item[2].center(10), item[3].center(6), item[4].center(6),
                  item[5].center(4), item[6].center(6),
                  item[7].center(15), item[8].center(15), item[9].center(6), item[10].center(4), item[11].center(20))
    else:
        print("\n")
        print("*"*50 + "\nNo entries found\n" + "*"*50)
        print("\n")
