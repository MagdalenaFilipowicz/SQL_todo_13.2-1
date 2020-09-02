import sqlite3

conn = sqlite3.connect("todo.db") #połączenie SQL z bazą danych
c = conn.cursor()

#Tworzymy tabelę
c.execute("""CREATE TABLE IF NOT EXISTS todo (
    title VARCHAR(150),
    description VARCHAR(350),
    status BIT NOT NULL
    )""")


many_todos = [
    ('Mycie okien', 'Umyć wszystie okna', '0'),
    ('Śniadanie', 'Zjeść owsiankę', '1'),
    ('Czytanie', 'Poczytać dzieciom', '0'),
    ('Zadanie Kodilla', 'Ogarnąć SQL', '1')
    ]

#c.executemany("INSERT INTO todo VALUES (?,?,?)", many_todos)
#c.execute("DELETE FROM todo WHERE rowid >= 1")

c.execute("SELECT rowid,* FROM todo")

 #drukuje całą bazę
#items = c.fetchall()
#for item in items:
#    print(item)


conn.commit()