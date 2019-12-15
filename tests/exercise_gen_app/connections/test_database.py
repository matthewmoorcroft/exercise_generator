from exercise_gen_app.connections.database import Database


class TestDatabase:

    def test_get_exercises_from_muscle_group(self):

        db = Database.get_instance()

        muscle_group = "Back"
        number_exercises = 4

        result = db.get_exercises_from_muscle_group(
            muscle_group=muscle_group,
            number_exercises=number_exercises
        )
        print(result['exercises'])
        assert "Success" in result['result']
