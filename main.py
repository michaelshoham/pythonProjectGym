class Gym:
    def __init__(self, name, address, phon):
        self.name = name
        self.address = address
        self.phon = phon
        self.another_phon = [phon]
        self.capacity = 20
        self.members = []
        self.sum_of_members = 0
        self.waiting_list = []

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, nwe_name):
        print('this is a name setter')
        self.name = nwe_name


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

    def is_capacity(self):
        if self.capacity - self.sum_of_members > 0:
            return True
        return False

    def sum_capacity(self):
        return self.capacity - self.sum_of_members

    def add_member(self, member):
        if not self.is_capacity():
            self.waiying_iist.append(member)

        elif self.is_capacity():
            self.members.append(member)
            self.sum_of_members += 1
            return 'the member is added'

        return 'sorry but there no mor space, we will call you when a space becomes available'

