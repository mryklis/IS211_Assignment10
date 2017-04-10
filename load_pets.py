import sqlite3

conn = sqlite3.connect('c:\users\mryklis\desktop\github\is211_assignment10\pets.db')

c = conn.cursor()

c.execute('INSERT INTO person (id, first_name, last_name, age)'
          'VALUES '
          '(1, 'James', 'Smith', 41),'
          '(2, 'Diana', 'Greene', 23),'
          '(3, 'Sara', 'White', 27),'
          '(4, 'William', 'Gibson', 23);')

c.execute('INSERT INTO pet (id, name, breed, age, dead)'
          'VALUES '
          '(), '
          '(), '
          '(), '
          '(), '
          '(), '
          '();')

##c.execute('INSERT INTO person_pet (person_id, pet_id) VALUES ();')

conn.commit()

conn.close()
