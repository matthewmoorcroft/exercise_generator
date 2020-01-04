from exercise_gen_app.model import exercise_generator


class TestExeciseGenerator:

    def test_exercise_builder(self):

        user_plan = exercise_generator.exercise_builder("3")
        print(user_plan)

        assert user_plan[0][0][0][0]['muscle_group'] in "Chest"
