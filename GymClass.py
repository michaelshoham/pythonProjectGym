from main import Entity
class Gym(Entity):
    def __init__(self, name, id, address, phon, email):

        super().__init__(self)

        self.capacity = 20
        self.members = []
        self.sum_of_members = len(self.members)
        self.waiting_list = []

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