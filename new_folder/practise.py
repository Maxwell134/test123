"""
Create a class Student

Create method setData and ask for name,phy,sci,eng,hind,math
Create method display and display all details
Create method totalMarks and display total marks (total - local variable)
Create method totalMarks2 and return total marks (total - local variable)
Create method updateName, enter your new name, then call display()
"""

class Student:

    def setData(self):
        self.name = input("Enter your name : ")
        self.phys = int(input("Enter your phys mark : "))
        self.eng = int(input("Enter your eng mark : "))
        self.hindi  = int(input("Enter your hindi mark "))
        self.math = int(input("Enter your math mark : "))

    def display(self):

       print(self.name)
       print(self.phys)
       print(self.eng)
       print(self.hindi)
       print(self.math)

    def totalMarks(self):
        total = sum([self.phys,self.eng,self.hindi, self.math])
        return total

    def totalMarks1(self):
        total1 = sum([self.phys,self.eng,self.hindi, self.math])
        return total1

    def update_name(self):
        self.name = input("Enter your name: ")



obj = Student()
obj.setData()
obj.display()

obj.update_name()
print(obj.totalMarks1())

obj.display()




