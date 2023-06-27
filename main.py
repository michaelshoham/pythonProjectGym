class Entity:

    def __init__(self, name, id, address, phon, email):
        self.name = name
        self.id = id
        self.email = email
        self.address = address
        self.phon = phon
        self.another_phon = [phon]

    def print_data(self):
        print('name:', self.name, '\t\t' 'id:', self.id, '\t\t' 'address:',
              self.address, '\t\t' 'phon numbers:', self.another_phon,
              '\t\t' 'email:', self.email)


        @property
        def name(self):
            return self.name

        @name.setter
        def name(self, nwe_name):
            print('this is a name setter')
            self.name = nwe_name

        @property
        def id(self):
            return self.id

        @id.setter
        def id(self, nwe_id):
            print('this is a name setter')
            self.id = nwe_id

        @property
        def email(self):
            return self.email

        @email.setter
        def email(self, nwe_email):
            print('this is a name setter')
            self.email = nwe_email

        @property
        def address(self):
            return self.address

        @address.setter
        def address(self, nwe_address):
            print('this is a address setter')
            self.address = nwe_address

        @property
        def phon(self):
            return self.phon

        @phon.setter
        def phon(self, nwe_phon):
            print('this is a phon setter')
            self.phon = nwe_phon

        @property
        def another_phon(self):
            return self.another_phon

        @another_phon.setter
        def another_phon(self, nwe_phon):
            print('this is a another_phon setter')
            self.another_phon = self.another_phon.append(nwe_phon)

def main():
    be_a_nunja = Entity('be_a_nunja', 200739977, 'begin', '0502626201', 'r@.com')
    be_a_nunja.print_data()
    print(be_a_nunja.address)
    be_a_nunja.address = 'menachem begin'
    be_a_nunja.print_data()

main()







