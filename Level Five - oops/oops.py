class bank_account:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def deposit(self, amount):
        if amount <= 0:
            print("Amount should be greater then 0")
        else :
            self.balance += amount
            print("Success")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount should be greater then 0")
        else :
            if self.balance < amount:
                print("Not enough balance")
            else:
                self.balance -= amount
                print("Success")
        
    def balance_check(self):
        print(f"Balance = {self.balance}")

acc1 = bank_account(500)

acc1.deposit(400)
acc1.withdraw(300)
acc1.balance_check()