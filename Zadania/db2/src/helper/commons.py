from Zadania.db2.src.properties import db_properties


def check_database(database_name):
    """
    Checks if given database exists.
    :return: True or False
    """
    if database_name in db_properties.database_structure:
        return True
    else:
        return False


def list_databases():
    """
    Displays all available databases.
    """
    if not db_properties.database_structure:
        print("There are no databases to display.")
    else:
        print("Available databases: ")
        for k in db_properties.database_structure.keys():
            print("\t" + k)


def get_database_columns(database_name):
    """
    Returns columns names as a list for given database.
    """
    return db_properties.database_structure[database_name]


def get_valid_field(database_name):
    """
    Asks for column name and check if provided value exists in given database.
    If exists returns column name.
    """
    while True:
        print(f"Available fields: {get_database_columns(database_name)}")
        field = str(input(f"Select field:\n")).lower().strip()
        if field not in get_database_columns(database_name):
            print("Provided field does not exist.")
        else:
            break
    return field
