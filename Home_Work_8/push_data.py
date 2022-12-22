from input_data import input_data
from write_data import write_data


def push_data():
    dict = input_data()

    write_data([dict.get("id"), dict.get("surname"), dict.get(
        "name"), dict.get("class"), dict.get("status")], "students.csv")

    write_data([dict["id"], dict["city"], dict["street"],
               dict["house"], dict["apartment"], dict["other"]], "address.csv")

    write_data([dict["id"], dict["row"], dict["col"]], "class.csv")
