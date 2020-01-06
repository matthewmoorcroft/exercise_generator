import psycopg2
from os import environ
from psycopg2.extras import RealDictCursor
import json
import logging

logger = logging.getLogger(__name__)


class Database:

    instance = None

    def __init__(self):
        try:
            connection =
            self.conn = psycopg2.connect(
                f"""dbname='{environ.get('RDS_DB_NAME')}'
                  user='{environ.get('RDS_USERNAME')}'
                  host='{environ.get('RDS_HOSTNAME')}'
                  password='{environ.get('RDS_PASSWORD')}'""")
        except psycopg2.Error:
            print("ERROR: Unable to connect to the database")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database()
        return cls.instance

    def add_exercise(self, name, muscle_group, area, tool):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)

        try:

            cur.execute("""INSERT INTO exercises (name,
                                                   muscle_group,
                                                   area,
                                                   tool)
                        VALUES (%(name)s,
                               %(muscle_group)s,
                               %(area)s,
                               %(tool)s)""", {
                'name': name,
                'muscle_group': muscle_group,
                'area': area,
                'tool': tool})

            self.conn.commit()
            cur.close()
            return json.dumps({'result': "ok"})
        except Exception as e:
            self.conn.rollback()
            cur.close()

            print(e)
            return json.dumps({'result': "Error: Failed to add user"})

    def get_exercises_from_muscle_group(self, muscle_group, number_exercises):

        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:

            cur.execute("""
                        SELECT *
                        FROM (
                            SELECT *,
                            rank() over (
                            partition by area order by RANDOM()
                            )
                            from exercises
                            where muscle_group=%(muscle_group)s
                            ) exercise_filter
                        where RANK<=%(number_exercises)s
                        order by rank limit %(number_exercises)s""",
                        {
                            'muscle_group': muscle_group,
                            'number_exercises': number_exercises
                        }
                        )
            rows = cur.fetchall()
            cur.close()

        except Exception as e:
            cur.close()

            print(e)
            return json.dumps({'result': "Error: Failed to extract exercises"})

        result = {}
        exercises = []
        for row in rows:
            exercise = {}
            exercise['name'] = row['name']
            exercise['muscle_group'] = row['muscle_group']

            logger.debug(exercise)
            exercises.append(exercise)

        result['exercises'] = exercises
        result['result'] = "Success: Ok"

        return result
