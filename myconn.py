import sqlite3

import pandas as pd


class MyConn(object):

    # what is the init method for?
    # it specifies things to do upon instantiation (creation)

    def __init__(self, filename=None):
        # what is self? 
        # a reference to the object
        self.__connection(filename=filename)

    def __connection(self, filename):
        self._conn = sqlite3.connect(filename)
        self.cursor = self._conn.cursor()
        print(f"cursor has been created for {filename}")

    def list_tables(self):
        query = """
                SELECT name
                FROM sqlite_master 
                WHERE type ='table';
                """

        res = self.cursor.execute(query).fetchall()
        table_names = [r[0] for r in res]
        return table_names

    @staticmethod
    def build_select_all_query(table_name=None):
        return f"select * from {table_name}"

    def select_all_from_table(self, table_name=None, load_df=False):
        query = self.build_select_all_query(table_name=table_name)
        if not load_df:
            res = self.cursor.execute(query).fetchall()
            return res

        else:
            df = pd.read_sql(query, self._conn)
            return df

    def list_table_columns(self, table_name):
        query = f"PRAGMA table_info({table_name});"

        return self.cursor.execute(query).fetchall()

    def close_connection(self):
        print("-" * 50)
        print("----closing connection to db----")
        print("-" * 50)
        self._conn.close()


# child class for one of our tables
# Employees

class Employees(MyConn):

    def __init__(self, filename=None):
        super(Employees, self).__init__(filename=filename)
        self.table_name = 'employees'

    def select_employee_names_by_office_code(self, office_code=None):
        query = f"select lastname, firstname, officecode from {self.table_name} where officecode is '{office_code}'"

        return self.cursor.execute(query).fetchall()


if __name__ == "__main__":
    my_conn = Employees(filename='data.sqlite')

    my_conn.select_employee_names_by_office_code(office_code=1)
