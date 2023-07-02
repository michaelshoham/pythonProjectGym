from TrainingLesson import TrainingLesson
class LessonManagement:
    EnrolledCustomers = []

    def __init__(self):
        pass

def enrolled_customer(self, customer):
    if len(self._enrolled_customers) < self._capacity:
        self._enrolled_customers.append(customer)
        print(f"Customer {customer.get_name()} enrolled in the {self._name} lesson.")
    else:
        print(f"The {self._name} lesson is already full. Customer {customer.get_name()} cannot enroll.")