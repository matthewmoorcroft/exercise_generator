import traceback
from connections.database import Database


def add_exercise():
    exercise_name = input("Name of exercise: ")
    body_part = input("Body part: ")
    part_area = input("Area: ")
    modality = input("Modality: ")

    db = Database.get_instance()
    db.add_exercise(
        exercise_name=exercise_name,
        body_part=body_part,
        part_area=part_area,
        modality=modality
    )


def main():
    while(True):
        print("1. Add exercise")
        print("2. Exit")

        options = {
            1: add_exercise,
            2: exit
        }
        choice = input("Choice: ")
        try:
            choice = int(choice)
            func = options[choice]
            func()
        except Exception:
            traceback.print_exc()
            print("You must choose option from the list")


if __name__ == "__main__":
    main()
