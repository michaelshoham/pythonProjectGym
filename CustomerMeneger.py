from Entity import Entity
from Customer import Customer

class CustomerManager:
    customers_lst = []



    def __init__(self):

        pass

    def add_customer(self, name, Id, address, phon, email, gender,
                 age=0, height=0, weight=0):
        new_customer = Customer(name, Id, address, phon, email, gender,
                  age, height, weight)
        CustomerManager.customers_lst.append(new_customer)



        return new_customer

def main():
    if __name__ == '__main__':
        manager = CustomerManager()
        manager.add_customer('Moshe', 200739977, 'yehoshua', '02523777', 'ksjdl@.com', 'mail')
        for elem in manager.customers_lst:
            print(elem.customer_id)




main()