from Zadania.db2.src.dao.database_manager import DbManager
from Zadania.db2.src.helper import commons
from Zadania.db2.src.properties import db_properties

while True:
    db_operation = input('''Choose option:
                         l  - list databases
                         c - choose database
                         q  - exit\n ''').lower().strip()
    if db_operation == "l":
        commons.list_databases()
    elif db_operation == "c":
        database_name = input("Provide database name:\n").lower().strip()
        if not commons.check_database(database_name):
            print(f"Database '{database_name}' does not exist.")
            pass
        else:
            db = DbManager(database_name)
            while True:
                operation = input(f'''Select option for '{db.db_name}' database:
                                  l - list database
                                  a - add new row
                                  s - search
                                  r - remove entry by name
                                  c - count by key and value
                                  d - clear database
                                  q - exit\n''').lower().strip()

                if operation == "l":
                    data = db.get_all_data()
                    if not data:
                        print(f"Database '{db.db_name}' is empty.")
                    else:
                        for row in data:
                            print(row)

                elif operation == "a":
                    row = {}
                    for i in db_properties.database_structure[db.db_name]:
                        row[i] = input(f'{i}: ').lower().strip()
                    db.add_database_entry(row)
                    print(f"Row {row} added to the '{db.db_name}' database.")

                elif operation == "s":
                    field = commons.get_valid_field(db.db_name)
                    value = input("Search value:\n").lower().strip()
                    data = db.search(field, value)
                    if not data:
                        print("No results found.")
                    else:
                        for row in data:
                            print(row)

                elif operation == "r":
                    field = commons.get_valid_field(db.db_name)
                    value = input("Delete by value:\n").lower().strip()
                    data = db.delete(field, value)
                    if not data:
                        print("No such data in db. Nothing has been removed.")
                    else:
                        print("The following data have been removed:")
                        for row in data:
                            print(row)

                elif operation == "c":
                    field = commons.get_valid_field(db.db_name)
                    value = str(input("Find by value:\n")).lower().strip()
                    count = db.count(field, value)
                    print(f"Number of results found: {count}.")

                elif operation == "d":
                    db.clear_database()
                    print(f"Database '{db.db_name}' has been cleared.")
                elif operation == "q":
                    print("Exiting..")
                    break
                else:
                    print("Unsupported option.")
    elif db_operation == "q":
        print("Exiting..")
        break
    else:
        print("Unsupported option.")
