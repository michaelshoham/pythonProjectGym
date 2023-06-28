from Entity import Entity
class Customer(Entity):
    customers_id = 1


    def __init__(self, name, Id, address, phone, email, gender,
                 age=0, height=0, weight=0):
        super().__init__(name, Id, address, phone, email)
        self.__age = 0
        self.__height = 0
        self.__weight = 0
        self.__gender = gender
        self.__customer_id = Customer.customers_id
        Customer.customers_id += 1
        self.__payment_plan = ''


    @property
    def payment_plan(self):
        return self.__payment_plan

    @payment_plan.setter
    def payment_plan(self, nwe_payment_plan):
        print('this is a payment_plan setter')
        self.__payment_plan = nwe_payment_plan



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

    @property
    def customer_id(self):
        return self.__customer_id



    def print(self):
        super.print_data(), print(self.gender, self.age, self.height, self.weight, self.payment_plan)



