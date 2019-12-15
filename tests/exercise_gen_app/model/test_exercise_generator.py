from exercise_gen_app.model import exercise_generator


class TestExeciseGenerator:

    # def test_get_exercises_from_muscle_group():
    #     print()
    #
    # def test_day_builder():
    #     print()
    #
    # def test_week_builder():
    #     print()
    #
    # def test_month_builder():
    #     print()

    def test_exercise_builder():

        user_plan = exercise_generator.exercise_builder(3)
        print(user_plan)

        assert user_plan[0][0][0]['muscle_group'] in "Chest"
