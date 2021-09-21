from connection.pg_connection import make_pg_pool



def migrate():
    conn = make_pg_pool()
    cursor = conn.cursor()
    
    