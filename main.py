class Entity:

    def __init__(self, name, id, address, phone, email):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__address = address
        self.__phone = phone
        self.__another_phone = [phone]



    @property
    def name(self):
        return self.__name

    @name.setter
    def _name(self, nwe_name):
        self.__name = nwe_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nwe_id):
        self.__id = nwe_id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nwe_email):
        self.__email = nwe_email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, nwe_address):
        self.__address = nwe_address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, nwe_phone):
        self.__phone = nwe_phone

    @property
    def another_phone(self):
        return self.__another_phone

    @another_phone.setter
    def another_phone(self, nwe_phone):
        self.__another_phone = self.__another_phon.append(nwe_phone)

    def print_data(self):
        print('name:', self.name, '\t\t' 'id:', self.id, '\t\t' 'address:',
              self.address, '\t\t' 'phon numbers:', self.another_phone,
              '\t\t' 'email:', self.email)


def main():
    be_a_nunja = Entity('be_a_nunja', 200739977, 'begin', '0502626201', 'r@.com')
    be_a_nunja.print_data()
    print(be_a_nunja.address)
    be_a_nunja.address = 'menachem begin'
    be_a_nunja.print_data()

# main()







