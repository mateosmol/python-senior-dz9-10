import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", timeout=5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Animals (name TEXT, type TEXT);")
cur.execute("DELETE FROM Animals;")
connection.commit()

cur.execute("INSERT INTO Animals (name, type) VALUES ('Лев', 'Ссавець')")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Крокодил', 'Плазун')")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Орел', 'Птах')")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Морська черепаха', 'Плазун')")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Мавпа', 'Ссавець')")
connection.commit()

# Маніпуляція 1 (Змініть назву звіра "Орел" на "Сокіл")
cur.execute("UPDATE Animals SET name='Сокіл' WHERE rowid=3;")
connection.commit()

# Маніпуляція 2 (Виберіть всіх звірів типу "Ссавець")
cur.execute("SELECT name FROM Animals WHERE type='Ссавець';")
for i in cur.fetchall():
    print(i)

print("")
# Маніпуляція 3 (Виведіть всі записи про звірів)
cur.execute("SELECT name, type FROM Animals;")
for i in cur.fetchall():
    print(i)

connection.close()