from Zadania.db2.src.helper.connection_manager import ConnectionManager
import pickle
import os


class DbManager(object):

    db_dir = os.path.join(os.path.abspath('..'), "db_files")

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = os.path.join(DbManager.db_dir, db_name+".dat")

    def get_all_data(self):
        """
        Returns all data from db as a list
        """
        all_data = []
        database = ConnectionManager().open_database_rb(self.db_path)
        if database is not None:
            while True:
                try:
                    all_data.append(pickle.load(database))
                except EOFError:
                    break
            ConnectionManager().close_database(database)
        return all_data

    def add_database_entry(self, row):
        """
        Adds given row to database.
        """
        database = ConnectionManager().open_database_ab(self.db_path)
        pickle.dump(row, database)
        ConnectionManager().close_database(database)

    def search(self, field, value):
        """
        Returns a list with all database rows where
        for column name = 'field' there is value = 'value'
        """
        searched_data = []
        all_data = self.get_all_data()
        if all_data:
            for i in all_data:
                if i.get(field) == value:
                    searched_data.append(i)
        return searched_data

    def delete(self, field, value):
        """
        Creates copy of db.
        Creates new version of db without rows
        where given field has value = given value.
        Returns a list of deleted rows.
        """
        all_data = self.get_all_data()
        deleted_data = []
        if all_data:
            try:
                os.remove(self.db_path+"_old")
            except FileNotFoundError:
                pass
            os.rename(self.db_path, self.db_path+"_old")
            deleted_data = []
            try:
                for i in all_data:
                    if i.get(field) != value:
                        self.add_database_entry(i)
                    else:
                        deleted_data.append(i)
            except Exception:
                os.rename(self.db_path+"_old", self.db_path)
        return deleted_data

    def count(self, field, value):
        """
        Returns number of rows where
        given field has value = given value.
        """
        data = self.search(field, value)
        if not data:
            return 0
        else:
            return len(data)

    def clear_database(self):
        """
        Creates new empty file.
        """
        ConnectionManager().open_database_wb(self.db_path)

    def __str__(self):
        return f"Database '{self.db_name}' under {self.db_path} path"
