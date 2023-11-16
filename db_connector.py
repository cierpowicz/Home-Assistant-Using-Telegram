import mysql.connector






class RaspberryConnector:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "192.168.1.77",
            user = "maczo1928all",
            passwd = "Pomidor13",
            database = "siemanko_test")
        
        self.cursor = self.conn.cursor()

        self.program_name = "Polaczenie z Raspberry"


    def insert_data(self, temp, wilg,gleba,):
        self.cursor.execute('INSERT INTO plant_02 (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()

    def close(self):
        self.conn.close()

raspberry_connection_01 = RaspberryConnector()


raspberry_connection_01.create_table()
raspberry_connection_01.close()








"""
class DBConnector:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')
        self.conn.commit()

    def insert_data(self, name, age):
        self.cursor.execute('INSERT INTO my_table (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()

    def delete_data(self, id):
        self.cursor.execute('DELETE FROM my_table WHERE id = ?', (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
"""
