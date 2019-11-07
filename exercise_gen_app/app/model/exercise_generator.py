from connections.database import Database


def get_exercise_from_bodypart(body_part, priority):
    db = Database.get_instance()

    db.get_exercise(body_part)


def day_builder(muscle_group):
    day = []
    for muscle in muscle_group:
        exercise = get_exercise_from_bodypart(
            body_part=muscle['body_part'],
            priority=muscle['priority']
        )

        day.append(exercise)


def week_builder():
    return


def month_builder():
    return


def exercise_builder():

    table = [
        {

        }
    ]
