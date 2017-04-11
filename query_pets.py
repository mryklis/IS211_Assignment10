import sqlite3

def person_record(rec):
    conn = sqlite3.connect('c:\users\mryklis\desktop\github\is211_assignment10\pets.db')

    c = conn.cursor()
    try:
        c.execute('SELECT * FROM person WHERE  id = {}'.format(rec))

        d = c.fetchone()

        print '{} {}, {} years old.'.format(d[1], d[2], d[3])


        c.execute('SELECT pet.name, pet.breed, pet.age, pet.dead FROM person_pet '
                  'LEFT JOIN pet ON person_pet.pet_id = pet.id '
                  'LEFT JOIN person ON person.id = person_pet.person_id '
                  'WHERE person_pet.person_id = {}'.format(rec))

        a = c.fetchall()
        if len(a) == 1:
            print '{} {} owned {}, a {}, that was {} years old'.format(d[1], d[2], a[0][0], a[0][1], a[0][2])
        elif len(a) > 1:
            print '{} {} owned {}, a {}, that was {} years old'.format(d[1], d[2], a[0][0], a[0][1], a[0][2])
            print '{} {} owned {}, a {}, that was {} years old'.format(d[1], d[2], a[1][0], a[1][1], a[1][2])
    except TypeError:
        print 'This person record does not exist'

    conn.close()

if __name__ == '__main__':
    i = 0
    while int(i) != -1:
        i = raw_input('Please enter person ID # (positive numbers only for records. enter -1 to exit)')
        if int(i) >= 1:
            person_record(i)
        elif int(i) == -1:
            exit()
