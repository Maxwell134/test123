# # class Student:
# #     def __init__(self, name: str, age: int):
# #         self.name = name
# #         self.age = age
# #
# #     def display(self):
# #         print(f"Name is {self.name}")
# #         print(f"Age is {self.age}")
# #
# #
# # s1 = Student("Anirudh", 55)
# # s1.display()
#
#
# """
# Make a class Employee
#
# Class variable should be asked from user
# They should be name,age,gender,department,experience,role
# Employee ID should be generated automatically and should
# be ALNUM (8 characters) - TH78AC65, 8909JH76
#
# Methods
# displayBasic() = Print details about emp_id,name,age,gender
# displayInfo() = Print deptmnt,exp,role
# changeDepartment() = Ask new department, and replace
# changeExp() = Ask new experience, and replace
# changeRole() = Ask new role, and replace
# """
# import random, string
#
#
# def generateRandomID():
#     return "".join(
#         random.choice(string.ascii_uppercase + string.digits) for _ in range(8)
#     )
#
#
# class Employee:
#     def __init__(self):
#         self.employeeId = generateRandomID()
#         self.name = input("Enter your name = ")
#         self.age = int(input("Enter your age = "))
#         self.gender = input("Enter your gender = ")
#         self.department = input("Enter your department = ")
#         self.experience = int(input("Enter your experience = "))
#         self.role = input("Enter your role = ")
#
#     def displayBasic(self):
#         print(f"Employee ID = {self.employeeId}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")
#
#     def displayInfo(self):
#         print(f"Department = {self.department}")
#         print(f"Experience = {self.experience}")
#         print(f"Role = {self.role}")
#
#     def changeDepartment(self):
#         self.department = input("Enter new department = ")
#
#     def changeExp(self):
#         self.experience = int(input("Enter new experience = "))
#
#     def changeRole(self):
#         self.role = input("Enter your new role = ")
#
#
# e1 = Employee()
# e1.displayBasic()
# e1.displayInfo()
# e1.changeDepartment()
# e1.changeExp()
# e1.changeRole()
# e1.displayBasic()
# e1.displayInfo()
#
# class Author:
#     def __init__(self) -> None:
#         self.name: str = input("Enter name = ")
#         self.age: int = int(input("Enter age = "))
#         self.books: list[str] = []
#
#     def displayInfo(self) -> None:
#         # Display name age
#         pass
#
#     def displayBooks(self) -> None:
#         # Iterate in self.books and display
#         # Each book
#         pass
#
#     def addBook(self) -> None:
#         # Ask book name and insert at 0 position
#         pass





class Author:
    def __init__(self):
        self.name: str = input("Enter name: ")
        self.age: int = int(input("Enter age: "))
        self.books: list[str] = []

    def displayInfo(self) -> None:
        print(f"Author: {self.name}")
        print(f"Age: {self.age}")

    def displayBooks(self) -> None:
        if not self.books:
            print("No books by this author.")
        else:
            print("Books by this author:")
            book_list = ", ".join(self.books)
            print(book_list)

    def addBook(self) -> None:
        book_name = input("Enter the book name: ")
        self.books.append(book_name)
        print(f"{book_name} has been added.")



author = Author()

while True:
    print("\nMenu:")
    print("1. Display author information")
    print("2. Display books by the author")
    print("3. Add a book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        author.displayInfo()
    elif choice == "2":
        author.displayBooks()
    elif choice == "3":
        author.addBook()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")





# import datetime
#
# from datetime import datetime

"""
Get current date with time
add time
subtract time
get difference between two dates
"""