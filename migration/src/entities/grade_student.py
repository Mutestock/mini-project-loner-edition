
from entities.entity_abstract import AbstractEntity
from connection.pg_connection import make_pg_pool
from utils.config import GRADES_STUDENTS_MIGRATIONS
from utils.query_utils import get_down_sql, get_up_sql


class GradeStudent(AbstractEntity):
    grade_id: int
    student_id: int

    def __init__(self, grade_id, student_id):
        self.grade_id = grade_id
        self.student_id = student_id

    def insert_query(self) -> None:
        conn = make_pg_pool()
        cursor = conn.cursor()
        query = f"INSERT INTO grades_students (grade_id, student_id) VALUES ({self.grade_id}, {self.student_id});"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def create_table() -> None:
        conn = make_pg_pool()
        cursor = conn.cursor()
        try:
            cursor.execute(get_up_sql(GRADES_STUDENTS_MIGRATIONS))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def drop_table() -> None:
        conn = make_pg_pool()
        cursor = conn.cursor()
        try:
            cursor.execute(get_down_sql(GRADES_STUDENTS_MIGRATIONS))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
