class RegularCustomer:
    def __init__(self, price):
        self.__price = price


    def get_services(self):
        return self._services

    def set_services(self, services):
        self._services = services


class PremiumCustomer(RegularCustomer):
    def __init__(self, price):
        super().__init__(price)
        self._additional_features = []


    def get_additional_features(self):
        return self._additional_features

    def set_additional_features(self, additional_features):
        self._additional_features = additional_features

