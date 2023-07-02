class TrainingLesson:
    Lesson_id = 1
    def __init__(self, name, time, capacity):
        self.__lesson_id = TrainingLesson.Lesson_id
        TrainingLesson.Lesson_id += 1
        self.__name = name
        self.__time = time
        self.__capacity = capacity


    @property
    def lesson_id(self):
        return self.__lesson_id

    @lesson_id.setter
    def lesson_id(self, nwe_lesson_id):
        self.lesson_id = nwe_lesson_id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nwe_name):
        self.__name = nwe_name


    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def enrolled_customer(self):
        return self.__enrolled_customers

    @enrolled_customer.setter
    def enrolled_customer(self, new_enrolled_customer):
         self.__enrolled_customer = new_enrolled_customer



    def display_details(self):
        print(f"Lesson: {self.name}")
        print(f"Time: {self.time}")
        print(f"Capacity: {len(self.enrolled_customers)}/{self.capacity}")
        print("Enrolled Customers:")
        for customer in self.enrolled_customers:
            print(f"- {customer.name()}")

