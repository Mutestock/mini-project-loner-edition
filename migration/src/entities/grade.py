
from entities.entity_abstract import AbstractEntity
from connection.pg_connection import make_pg_pool
from utils.config import GRADES_MIGRATIONS
from utils.query_utils import get_down_sql, get_up_sql


class Grade(AbstractEntity):
    name: str

    def __init__(self, name):
        self.name = name

    def insert_query(self) -> None:
        conn = make_pg_pool()
        cursor = conn.cursor()
        query = f"INSERT INTO grades (name) VALUES ('{self.name}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def create_table() -> None:
        conn = make_pg_pool()
        cursor = conn.cursor()
        try:
            cursor.execute(get_up_sql(GRADES_MIGRATIONS))
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
            cursor.execute(get_down_sql(GRADES_MIGRATIONS))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
