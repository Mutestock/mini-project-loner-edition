from logic.pg_exec import migrate_up, migrate_down
import time

def main() -> None:
    time.sleep(10.0)
    migrate_down()
    migrate_up()

if __name__ =="__main__":
    main()
