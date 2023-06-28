class TrainingLesson:
    def __init__(self, lesson_id, name, time, capacity):
        self._lesson_id = lesson_id
        self._name = name
        self._time = time
        self._capacity = capacity
        self._enrolled_customers = []

    def get_lesson_id(self):
        return self._lesson_id

    def set_lesson_id(self, lesson_id):
        self._lesson_id = lesson_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def enroll_customer(self, customer):
        if len(self._enrolled_customers) < self._capacity:
            self._enrolled_customers.append(customer)
            print(f"Customer {customer.get_name()} enrolled in the {self._name} lesson.")
        else:
            print(f"The {self._name} lesson is already full. Customer {customer.get_name()} cannot enroll.")

    def display_details(self):
        print(f"Lesson: {self._name}")
        print(f"Time: {self._time}")
        print(f"Capacity: {len(self._enrolled_customers)}/{self._capacity}")
        print("Enrolled Customers:")
        for customer in self._enrolled_customers:
            print(f"- {customer.get_name()}")

