class Payment:
    def calculate_fee(self, customer):
        if isinstance(customer, RegularCustomer):
            return 50
        elif isinstance(customer, PremiumCustomer):
            return 100

    def generate_invoice(self, customer):
        fee = self.calculate_fee(customer)
        invoice = f"Invoice for Customer {customer.get_name()}\nPayment Plan: {customer.get_payment_plan()}\nFee: {fee} USD"
        return invoice
