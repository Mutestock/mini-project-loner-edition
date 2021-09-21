from logic.pg_exec import migrate_up, migrate_down

def main() -> None:
    migrate_down()
    migrate_up()

if __name__ =="__main__":
    main()