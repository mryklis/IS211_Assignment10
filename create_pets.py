import sqlite3

conn = sqlite3.connect('c:\users\mryklis\desktop\github\is211_assignment10\pets.db')

c = conn.cursor()

c.execute('CREATE TABLE person (id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT);')

c.execute('CREATE TABLE pet (id INT PRIMARY KEY, name TEXT, breed TEXT, age INT, dead INT);')

c.execute('CREATE TABLE person_pet (person_id INT, pet_id INT);')

conn.commit()

conn.close()
