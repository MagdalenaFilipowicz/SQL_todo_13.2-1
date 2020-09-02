import sqlite3 
from sqlite3 import Error


class TodosSQLite():
    def __init__(self,data_base):
        self.conn = None
        try:
            self.conn = sqlite3.connect(data_base, check_same_thread=False)
            if self.conn is not None:
                self.conn.cursor().execute("""CREATE TABLE IF NOT EXISTS todo (
                                            title VARCHAR(150),
                                            description VARCHAR(350),
                                            status BIT NOT NULL
                                            )""")
            self.cur = self.conn.cursor()
        except Error as e:
            print(e)

    def all(self):
        result = self.cur.execute("SELECT * FROM todo")
        return result.fetchall()

    def get(self, id):
        result = self.cur.execute(f"SELECT * FROM todo WHERE id={id}")
        return result.fetchone()
 
    def create(self, table):
        sql = '''INSERT INTO todo (title, description, done)
                    VALUES(?,?,?)'''
        result = self.cur.execute(sql, table)
        self.conn.commit()
        return result.lastrowid
    
    def update(self, id, table,**k):
        sql = f''' UPDATE todos
                    SET title = ?, description = ?, status = ?
                    WHERE id = {id}'''
        try:
            self.cur.execute(sql, table)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
   
    def delete_where(self, **kwargs):
        """
        Delete from table where attributes from
        :param kwargs: dict of attributes and values
        :return:
        """
        qs = []
        values = tuple()
        for k, v in kwargs.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)

        sql = f'DELETE FROM todo WHERE {q}'
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()
        print("Deleted")



data_base = "todo.db"
todos = TodosSQLite(data_base)

if __name__ == "__main__":
   
   db_file = "todo.db"
   print_table = TodosSQLite(db_file)
   
#print(todos.all())
#for item in todos.all():
#    print(item)

#print_table.update(table = todos, id = 2, data = ["Sniadanie","Zjeść kanapkę", "1"])

#for item in todos.all():
#    print(item)