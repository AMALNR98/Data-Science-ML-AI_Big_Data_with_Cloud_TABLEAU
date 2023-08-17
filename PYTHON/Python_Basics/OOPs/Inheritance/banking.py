# Banking

# Class Bank:
#   bank name(instance variable)
#   account creation(name, account_number)

#   acc_create(name, acc_number)

#       min_balance = 5000
#       total_balance = self.min-balance

#   cash_deposit(amount)
#       print("------")
#   cash_with (amount) withdrew
#       print("-------")

class Bank:
    bank_name = "X-bank"

    def account_creation(self, name, account_number):
        self.name = name
        self.account_number = account_number

        self.minimun_balance = 5000
        self.total_balance = self.minimun_balance



    def cash_depsit(self, deposit_amount):
        self.amount = deposit_amount
        self.total_balance = self.amount + self.minimun_balance
        print(f"your{Bank.bank_name} , acc has been credited the amount {self.amount} available balance is {self.total_balance}")

    def cash_withdrew(self, withdrew_amount):
        self.withdrew_amount = withdrew_amount
        if self.withdrew_amount > self.total_balance:
            print("Insufficient balance")
        else:
            self.total_balance = self.total_balance - self.withdrew_amount
            print(f" Your,{Bank.bank_name}, account ahss been debited the abount{self.withdrew_amount} available balance is {self.total_balance}")




obj_1 = Bank()
obj_1.account_creation("amal",1)
obj_1.cash_depsit(500000)
obj_1.cash_withdrew(7000)