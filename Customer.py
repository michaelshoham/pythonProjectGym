from main import Entity
class Customer(Entity):
    def __init__(self, name, Id, address, phon, email, gender,
                 age=0, height=0, weight=0):
        super.__init__(Customer)
        self.__age = 0
        self.__height = 0
        self.__weight = 0
        self.__gender = gender


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, nwe_age):
        print('this is a age setter')
        self.__age = nwe_age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, nwe_height):
        print('this is a height setter')
        self.__height = nwe_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, nwe_weight):
        print('this is a weight setter')
        self.__weight = nwe_weight

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        print('this is a gender setter')
        self.__gender = new_gender

# def main():
#     if __name__ == '__main__':
#         Alecs = Customer()