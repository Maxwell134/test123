from random import randint

class Bank:
    def createAccount(self):
        self.accountNumber = randint(100000, 999999)
        self.name = input("Enter your account name = ")
        self.balance = 0
        self.branch = input("Enter branch name = ")

    def createAccount2(self, name: str, branch: str = "City Light", balance: int = 0):
        self.accountNumber = randint(100000, 999999)
        self.name = name
        self.balance = balance
        self.branch = branch

    def display(self):
        print(f"Account number = {self.accountNumber}")
        print(f"Account name = {self.name}")
        print(f"Account balance = {self.balance}")
        print(f"Account branch = {self.branch}")


b1 = Bank()

b1.createAccount2(name="Anirudh")
b1.display()


from random import randint


class Bank:
    """accountNumber
    amt
    """

    def createAccount(self):
        self.accountNumber = randint(100000, 999999)
        self.name = input("Enter your account name = ")
        self.balance = 0
        self.branch = input("Enter branch name = ")

    def display(self):
        print(f"Account number = {self.accountNumber}")
        print(f"Account name = {self.name}")
        print(f"Account balance = {self.balance}")
        print(f"Account branch = {self.branch}")

    def showBalance(self):
        print(f"Your current balance is = {self.balance}")

    def withdraw(self):
        amt = int(input("Enter amount to withdraw = "))
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amt
            self.showBalance()

    def deposit(self):
        amt = int(input("Enter amount to deposit = "))
        self.balance += amt
        self.showBalance()


b1 = Bank()
b2 = Bank()

b1.createAccount()
b2.createAccount()
b1.display()
b1.withdraw()
b1.deposit()
b1.display()
b2.display()

class Student:
    # Dunder
    def __init__(self):  # Constructor (Memory Initialize)
        self.name = input("Enter student name =")
        self.age = int(input("Enter student age ="))
        self.gender = input("Enter student gender =")
        self.phone = int(input("Enter student phone ="))

    def display(self):
        print(f"Name = {self.name}, age = {self.age}, gender= {self.gender}")


s1 = Student()
s2 = Student()

b = []

for i in range(3):
    x = Bank()
    b.append(x)

for i in range(3):
    b[i].display()