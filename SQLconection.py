
class SQL3:
    import sqlite3


    def __init__(self):
        import sqlite3
        self.con = sqlite3.connect('Gym.db')
        self.cur = self.con.cursor()


    def CreateTable(self, table, my_tuple):
            import sqlite3
            con = sqlite3.connect('Gym.db')
            cur = con.cursor()

            try:
                cur.execute(f'CREATE TABLE {table} ({my_tuple})')
                con.commit()
            except sqlite3.OperationalError as e:
                print(e, 'this is a problem')


    def check_id_exists(self, table, ID):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"SELECT ID FROM {table} WHERE id = ?", (ID,))
        row = cur.fetchone()

        if row is not None:
            return True
        else:
            return False


    def display_records(self, table):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    def remove_duplicate_records(self, table):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"SELECT id, COUNT(*) FROM {table} GROUP BY id HAVING COUNT(*) > 1")
        duplicate_ids = cur.fetchall()


        cur.execute(f"""
            DELETE FROM {table}
            WHERE ROWID NOT IN (
                SELECT MIN(ROWID)
                FROM {table}
                GROUP BY id
            )
        """)
        con.commit()
        print("Duplicate records removed.")


    def get_record(self, table, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table} WHERE id = ?", (Id,))
        duplicate_ids = cur.fetchall()

        return duplicate_ids

    def remove_record(self, table, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table} WHERE id = ?", (Id,))

        cur.execute(f"DELETE FROM {table} WHERE id = ?", (Id,))
        con.commit()
        print("Record deleted successfully.")


    def remove_one_record(self, table, column, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(f"UPDATE {table} SET {column} = NULL WHERE id = ?", (Id,))

        con.commit()
        print(f"Item '{column}' for ID '{table}' removed successfully.")

        con.close()

    import sqlite3

    def add_or_chinge_item_by_id(self, table, column, item_value, id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()

        cur.execute(f"UPDATE {table} SET {column} = ? WHERE id = ?", (item_value, id))
        con.commit()

        print(f"Item '{column}' with value '{item_value}' added successfully for customer ID '{id}'.")

        con.close()



    # def return_like_instance(self, class_instance, table, id):
    #     import sqlite3
    #     con = sqlite3.connect('Gym.db')
    #     cur = con.cursor()
    #     cur.execute(f"SELECT id FROM {table} WHERE id = ?", (id,))
    #     row = cur.fetchone()
    #     nwe_instance = class_instance.

def main():
    a = SQL3
if __name__ == '__main__':
    main()