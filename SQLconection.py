import sqlite3
con = sqlite3.connect('tutorial.db')
cur = con.cursor()
cur.execute('CREATE TABLE CustomersGym(name, Id, address, phone, email, gender,age, height, weight)')
cur.execute("""
INSERT INTO customer VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2, 'oioij'),
        ('And Now for Something Completely Different', 1971, 7.5, 'ouhiuhh')
""")

con.commit()


res = cur.execute("SELECT * FROM customer")
print(res.fetchall())