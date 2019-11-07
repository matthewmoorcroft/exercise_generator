import psycopg2
import json


class Database:

    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                """dbname='exercise_gen'
                  user='postgres'
                  host='localhost'
                  password='1245788956'""")
        except psycopg2.Error:
            print("ERROR: Unable to connect to the database")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database()
        return cls.instance

    def add_exercise(self, exercise_name, body_part, part_area, modality):

        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO exercises (exercise_name,
                                                   body_part,
                                                   part_area,
                                                   modality)
                        VALUES (%(exercise_name)s,
                               %(body_part)s,
                               %(part_area)s,
                               %(modality)s)""", {
                'exercise_name': exercise_name,
                'body_part': body_part,
                'part_area': part_area,
                'modality': modality})

            self.conn.commit()
            cur.close()
            return json.dumps({'result': "ok"})
        except Exception as e:
            self.conn.rollback()
            cur.close()

            print(e)
            return json.dumps({'result': "Error: Failed to add user"})
