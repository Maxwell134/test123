# # class Student:
# #     name = "Tridib"
# #     age =  29
# #     gender = "Male"
# #
# # s1 = Student()
# # s2 = Student()
# #
# # print(s1.name)
# # print(s1.age)
# # print(s1.gender)
# # print(f"My name is {s1.name}")
#
# #
# # class Student:  #member /class
# #      x = "mintu"
# #
# #      def setData(self):    #Methods
# #          self.name = input("Enter  your name: ")
# #          self.age = int(input("Enter  your age: "))
# #          self.gender = input("Enter  your gender: ")
# #
# #      def display(self):
# #          print(f"My name is : {self.name}")
# #          print(f"My age  is : {self.age}")
# #          print(f"My gender is : {self.gender}")
# #
# #
# # obj = Student()
# # obj.setData()
# # obj.display()
# # print(obj.x)
#
#
# # class Student:
# #
# #     def setData(self):
# #         self.name = input("Enter your name: ")
# #         self.phys = int(input("Enter your physics mark: "))
# #         self.eng = int(input("Enter your English mark: "))
# #         self.hindi = int(input("Enter your Hindi mark: "))
# #         self.math = int(input("Enter your math mark: "))
# #
# #     def display(self):
# #         student_data = {
# #             "Name": self.name,
# #             "Physics": self.phys,
# #             "English": self.eng,
# #             "Hindi": self.hindi,
# #             "Math": self.math
# #         }
# #         return student_data
# #
# #     def totalMarks(self):
# #         total = sum([self.phys, self.eng, self.hindi, self.math])
# #         return total
# #
# #     def update_name(self):
# #         self.name = input("Enter your new name: ")
# #
# # # Create a list to store student objectsTe
# # students = []
# #
# # # Create and add data for 4 students
# # for i in range(2):
# #     obj = Student()
# #     obj.setData()
# #     students.append(obj)
# #
# #
# # tom = {}
# # # Display the details of each student in dictionary format
# # for i, student in enumerate(students, start=1):
# #     print(f"\nStudent {i} Details:")
# #     student_data = student.display()
# #     for key, value in student_data.items():
# #         print(f"{key}: {value}")
# #     print(f"Total Marks: {student.totalMarks()}")
#
# # from random import randint
# #
# # class Bank:
# #     """accountNumber
# #     amt
# #     """
# #
# #     def createAccount(self):
# #         self.accountNumber = randint(100000, 999999)
# #         self.name = input("Enter your account name = ")
# #         self.balance = 0
# #         self.branch = input("Enter branch name = ")
# #
# #     def display(self):
# #         print(f"Account number = {self.accountNumber}")
# #         print(f"Account name = {self.name}")
# #         print(f"Account balance = {self.balance}")
# #         print(f"Account branch = {self.branch}")
# #
# #     def showBalance(self):
# #         print(f"Your current balance is = {self.balance}")
# #
# #     def withdraw(self):
# #         amt = int(input("Enter amount to withdraw = "))
# #         if amt > self.balance:
# #             print("Insufficient balance")
# #         else:
# #             self.balance = self.balance - amt
# #             self.showBalance()
# #
# #     def deposit(self):
# #         amt = int(input("Enter amount to deposit = "))
# #         self.balance += amt
# #         self.showBalance()
# # b1 = Bank()
# # b2 = Bank()
# #
# # b1.createAccount()
# # b2.createAccount()
# # b1.display()
# # b1.withdraw()
# # b1.deposit()
# # b1.display()
# # b2.display()
#
# b = []
#
# for i in range(3):
#     x = Bank()
#     b.append(x)
#
# for i in range(3):
#     b[i].display()
#
# class Student:
#     # Dunder
#     def __init__(self):  # Constructor (Memory Initialize)
#         self.name = input("Enter student name =")
#         self.age = int(input("Enter student age ="))
#         self.gender = input("Enter student gender =")
#         self.phone = int(input("Enter student phone ="))
#
#     def display(self):
#         print(f"Name = {self.name}, age = {self.age}, gender= {self.gender}")
#
#
# s1 = Student()
# s2 = Student()
#

def rand_number():
    return randint(100000, 9999999)

from random import randint

class Bank:
    def __init__(self):
        self.accountNumber = rand_number()
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


accounts: list[Bank] = []

while True:
    print("\n1) Add an account")
    print("2) View all accounts")
    print("3) Search a account by account number")
    print("4) Deposit into your account")
    print("5) Withdraw into your account")
    print("6) Transfer")
    print("7) Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        # accounts.insert(0, obj)
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts added till yet")
        else:
            for i in range(0, len(accounts)):
                accounts[i].display()
    elif choice == 3:
        acc_no = int(input("Enter account number = "))
        for i in range(0, len(accounts)):
            if accounts[i].accountNumber == acc_no:
                accounts[i].display()
                break
        else:
            print("No accounts found")
    elif choice == 4:
        acc_no = int(input("Enter account number = "))
        for i in range(0, len(accounts)):
            if accounts[i].accountNumber == acc_no:
                accounts[i].deposit()
                break
        else:
            print("No accounts found")
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
