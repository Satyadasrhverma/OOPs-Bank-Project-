class Bank:
    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.balance = balance
        self.transactions = []

    def debit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        self.transactions.append(f"Debited Rs {amount}")
        return f"Rs {amount} debited successfully"

    def credit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        self.balance += amount
        self.transactions.append(f"Credited Rs {amount}")
        return f"Rs {amount} credited successfully"

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions
