
class ConnectionManager(object):

    def open_database_rb(self, db_path):
        try:
            return open(db_path, "rb+")
        except FileNotFoundError as e:
            return None

    def open_database_wb(self, db_path):
        return open(db_path, "wb+")

    def open_database_ab(self, db_path):
        return open(db_path, "ab+")

    def close_database(self, db_connection):
        db_connection.close()





