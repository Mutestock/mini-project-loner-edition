from logic.pg_exec import migrate_up, migrate_down
import time

# Sleep to allow postgres to start up in container
# Alternative would be wait-for-it.sh
def main() -> None:
    time.sleep(10.0)
    migrate_down()
    migrate_up()

if __name__ =="__main__":
    main()
