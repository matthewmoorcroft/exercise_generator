from ..connections.database import Database
import logging

logger = logging.getLogger(__name__)

plans = {
    '3': [
        [
            {
                'name': "Chest",
                'number_exercises': 3,
            },
            {
                'name': "Triceps",
                'number_exercises': 3,
            },
        ],
        [
            {
                'name': "Back",
                'number_exercises': 2,
            },
            {
                'name': "Biceps",
                'number_exercises': 2,
            },
            {
                'name': "Shoulders",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Legs",
                'number_exercises': 4,
            },
            {
                'name': "Abdominals",
                'number_exercises': 2,
            },
        ],
    ],
    '4': [
        [
            {
                'name': "Chest",
                'number_exercises': 4,
            },
            {
                'name': "Triceps",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Back",
                'number_exercises': 4,
            },
            {
                'name': "Biceps",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Legs",
                'number_exercises': 4,
            },
            {
                'name': "Abdominals",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Shoulders",
                'number_exercises': 2,
            },
            {
                'name': "Triceps",
                'number_exercises': 2,
            },
            {
                'name': "Biceps",
                'number_exercises': 2,
            },
        ],
    ],
    '5': [
        [
            {
                'name': "Legs",
                'number_exercises': 4,
            },
            {
                'name': "Abdominals",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Chest",
                'number_exercises': 4,
            },
            {
                'name': "Triceps",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Back",
                'number_exercises': 4,
            },
            {
                'name': "Biceps",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Legs",
                'number_exercises': 4,
            },
            {
                'name': "Abdominals",
                'number_exercises': 2,
            },
        ],
        [
            {
                'name': "Shoulders",
                'number_exercises': 2,
            },
            {
                'name': "Triceps",
                'number_exercises': 2,
            },
            {
                'name': "Biceps",
                'number_exercises': 2,
            },
        ],
    ]
}


def get_exercises_from_muscle_group(muscle_group, number_exercises):
    db = Database.get_instance()

    exercises = db.get_exercises_from_muscle_group(muscle_group=muscle_group,
                                                   number_exercises=number_exercises)
    return exercises


def day_builder(day):

    day_length = len(day)
    exercise_day = []
    for exercise in day:
        exercises = get_exercises_from_muscle_group(
            muscle_group=exercise['muscle_group'],
            number_exercises=exercise['number_exercises']
        )['exercises']

        exercise_day.append(exercises)
    return exercise_day


def week_builder(plan):
    week = []
    for day in plan:
        exercise_day = day_builder(day)
        week.append(exercise_day)

    return


def month_builder(plan):
    user_plan = []
    for x in range(0, 4):
        week = week_builder(plan)
        user_plan.append(week)
    return user_plan


def exercise_builder(days):

    plan = plans[days]

    user_plan = month_builder(plan)
    return user_plan
