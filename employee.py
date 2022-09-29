"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, commission=0):
        self.name = name
        self.pay = pay
        self.commission = commission

    def get_pay(self):
        if self.commission:
            return self.pay.calculate_pay()+self.commission.calculate_commission()
        else:
            return self.pay.calculate_pay()

    def __str__(self):
        if self.commission:
            return f"{self.name} works on a {str(self.pay)} and recieves a {str(self.commission)}.  Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a {str(self.pay)}.  Their total pay is {self.get_pay()}."

class Pay:
    def calculate_pay(self):
        return

class Salary(Pay):
    def __init__(self, amount):
        self.amount = amount

    def calculate_pay(self):
        return self.amount

    def __str__(self):
        return f"monthly salary of {self.amount}"

class ContractPay(Pay):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours*self.rate

    def __str__(self):
        return f"contract of {self.hours} hours at {self.rate}/hour"

class Commission:
    def calculate_commission(self):
        return

class Bonus(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def calculate_commission(self):
        return self.bonus

    def __str__(self):
        return f"bonus commission of {self.bonus}"

class ContractCommission(Commission):
    def __init__(self, nOfContracts, rate):
        self.nOfContracts = nOfContracts
        self.rate = rate

    def calculate_commission(self):
        return self.nOfContracts*self.rate

    def __str__(self):
        return f"commission for {self.nOfContracts} contract(s) at {self.rate}/contract"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Salary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ContractPay(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Salary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ContractPay(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Salary(2000), Bonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ContractPay(120, 30), Bonus(600))
