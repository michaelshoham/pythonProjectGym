
class SQL3:
    import sqlite3


    def __init__(self):
        import sqlite3
        self.con = sqlite3.connect('Gym.db')
        self.cur = self.con.cursor()
    def CreateTableCustomersGym(self):
        import sqlite3
        try:
            self.cur.execute('CREATE TABLE CustomersGym(name, Id, address, phone, email,'
                             ' gender, age, height, weight, customer_id, payment_plan)')
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)

    # def InsetIntoCustomersGym(self, name, Id, address, phone, email,
    #                           gender, age, height, weight, customer_id, payment_plan):
    #     import sqlite3

        # self.cur.execute('INSERT INTO CustomersGym VALUES(name= name, Id= Id, address= address, phone= phone, email= email,'
        #                  'gender= gender, age= age, height=height, weight= weight, customer_id= customer_id, payment_plan= payment_plan)')
        # return self.cur.execute("SELECT customer_id FROM CustomersGym WHERE id= Id ")


            # self.execute(""" customer VALUES(')""")
    # def get_information(self):
def maim():
    Tabel = SQL3()

    # Tabel.CreateTableCustomersGym()

maim()

# cur.execute("""INSERT INTO customer VALUES
        # ('Monty Python and the Holy Grail', 1975, 8.2, 'oioij'),
        # ('And Now for Something Completely Different', 1971, 7.5, 'ouhiuhh')""")

    # con.commit()


    # res = cur.execute("SELECT * FROM customer")
    # print(res.fetchall())