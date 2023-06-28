class RegularCustomer(Customer):
    def __init__(self, member_id, name, age, gender, customer_id, payment_plan, services):
        super().__init__(member_id, name, age, gender, customer_id, payment_plan)
        self._services = services

    def get_services(self):
        return self._services

    def set_services(self, services):
        self._services = services


class PremiumCustomer(Customer):
    def __init__(self, member_id, name, age, gender, customer_id, payment_plan, additional_features):
        super().__init__(member_id, name, age, gender, customer_id, payment_plan)
        self._additional_features = additional_features

    def get_additional_features(self):
        return self._additional_features

    def set_additional_features(self, additional_features):
        self._additional_features = additional_features

