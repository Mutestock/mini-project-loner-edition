from connection.pg_connection import make_pg_pool
from utils.config import MIGRATIONS_FOLDER_PATH


STUDENTS_MIGRATIONS = MIGRATIONS_FOLDER_PATH+"/students"
TEACHERS_MIGRATIONS = MIGRATIONS_FOLDER_PATH+"/teachers"
GRADES_MIGRATIONS = MIGRATIONS_FOLDER_PATH+"/grades"
GRADES_TEACHERS_MIGRATIONS = MIGRATIONS_FOLDER_PATH+"/grades_teachers"
GRADES_STUDENTS_MIGRATIONS = MIGRATIONS_FOLDER_PATH+"/grades_students"


def get_sql(folder: str, sql_script_type: str) -> str:
    filename = f"{folder}/{sql_script_type}.sql"
    content = ""
    with open(filename) as f:
        content = f.read()
    return content

def get_up_sql(folder: str) -> str:
    return get_sql(folder, "up")

def get_down_sql(folder: str) -> str:
    return get_sql(folder, "down")
    


def migrate_down() -> None:
    conn = make_pg_pool()
    
    cursor = conn.cursor()
    cursor.execute(get_down_sql(GRADES_STUDENTS_MIGRATIONS))
    cursor.execute(get_down_sql(GRADES_TEACHERS_MIGRATIONS))
    cursor.execute(get_down_sql(GRADES_MIGRATIONS))
    cursor.execute(get_down_sql(TEACHERS_MIGRATIONS))
    cursor.execute(get_down_sql(STUDENTS_MIGRATIONS))
    
    conn.commit()
    cursor.close()
    conn.close()


# Add new types here
def migrate_up() -> None:
    conn = make_pg_pool()
    
    cursor = conn.cursor()
    cursor.execute(get_up_sql(STUDENTS_MIGRATIONS))
    cursor.execute(get_up_sql(TEACHERS_MIGRATIONS))
    cursor.execute(get_up_sql(GRADES_MIGRATIONS))
    cursor.execute(get_up_sql(GRADES_STUDENTS_MIGRATIONS))
    cursor.execute(get_up_sql(GRADES_TEACHERS_MIGRATIONS))
    
    conn.commit()
    cursor.close()
    conn.close()
    

