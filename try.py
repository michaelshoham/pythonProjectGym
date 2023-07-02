import sqlite3
#
# con = sqlite3.connect('Gym.db')
# cur = con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY,
#             book_name TEXT,
#             author_name TEXT,
#             genre TEXT,
#             publishing_year INTEGER,
#             age_restriction TEXT,
#             number_of_pages INTEGER,
#             available TEXT)''')
import sqlite3

def create_table_with_autoincrement(YourTable, my_tuple):
    conn = sqlite3.connect('Gym.db')
    cur = conn.cursor()

    cur.execute(f'CREATE TABLE {YourTable} ({my_tuple})')

    conn.commit()
    conn.close()

# Call the function to create the table
create_table_with_autoincrement('try_taibl_2', ('id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                                ' name TEXT,'
                                                ' address TEXT,'
                                                ' phone TEXT,'
                                                ' email TEXT'))
