import sqlite3

conn = sqlite3.connect('c:\users\mryklis\desktop\github\is211_assignment10\pets.db')

c = conn.cursor()

c.execute('SELECT * FROM person_pet')

print c.fetchall()
conn.close()