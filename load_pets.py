import sqlite3

conn = sqlite3.connect('c:\users\mryklis\desktop\github\is211_assignment10\pets.db')

c = conn.cursor()

c.execute('''INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'James', 'Smith', 41),
(2, 'Diana', 'Greene', 23),
(3, 'Sara', 'White', 27),
(4, 'William', 'Gibson', 23);''')

c.execute('''INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Rusty', 'Dalmation', 4, 1),
 (2, 'Bella', 'Alaskan Malamute', 3, 0),
 (3, 'Max', 'Cocker Spaniel', 1, 0),
 (4, 'Rocky', 'Beagle', 7, 0),
 (5, 'Rufus', 'Cocker Spaniel', 1, 0),
 (6, 'Spot', 'Bloodhound', 2, 1);''')


c.execute('''INSERT INTO person_pet (person_id, pet_id) VALUES (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6);''')

conn.commit()

conn.close()
