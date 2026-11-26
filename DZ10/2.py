import sqlite3

connection = sqlite3.connect("FruitBasket.sl3", timeout=5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Fruits (name TEXT, color TEXT);")
cur.execute("DELETE FROM Fruits;")
connection.commit()

cur.execute("INSERT INTO Fruits (name, color) VALUES ('Яблуко', 'Червоне')")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Банан', 'Жовтий')")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Апельсин', 'Помаранчевий')")
connection.commit()

# Маніпуляція 1 (Змініть колір фрукта "Яблуко" на "Зелене")
cur.execute("UPDATE Fruits SET color='Зелене' WHERE name='Яблуко';")
connection.commit()

# Маніпуляція 2 (Виберіть всі фрукти жовтого кольору)
cur.execute("SELECT name FROM Fruits WHERE color='Жовтий';")
for i in cur.fetchall():
    print(i)

print("")
# Маніпуляція 3 (Виведіть всі записи про фрукти)
cur.execute("SELECT name, color FROM Fruits;")
for i in cur.fetchall():
    print(i)

connection.close()