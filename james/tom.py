# # f = open("dob.txt", "w")
# # f.write("Hello")
# # f.close()
#
# """
# Ask name, age, gender from user
# Filename = anri.txt
# my name is {}
# my gender is {}
# my age is {}
#
# """
# # def writeIntoFile(name, age, gender):
# #     f = open(f"{name}.txt", "w")
# #     f.write(f"My name is {name}\n")
# #     f.write(f"My age is {age}\n")
# #     f.write(f"My gender is {gender}\n")
# #     f.close()
# #
# #
# # name = input("Enter name = ")
# # age = int(input("Enter age = "))
# # gender = input("Enter gender = ")
# # writeIntoFile(name, age, gender)
# #
# # data = input("Enter: ")
# # filename = input("Enter filename : ")
# #
# # with open(f"{filename}.txt", "w") as f:
# #     f.write(data)
# #     print("Done")
#
# # def copy_file(source_file, destination_file):
# #     with open(source_file, "r") as f_source:
# #         data = f_source.read()
# #
# #     with open(destination_file, "w") as f_destination:
# #         f_destination.write(data)
# #
# # source_file = "tridib.txt"
# # destination_file = "mintu.txt"
# # copy_file(source_file, destination_file)
#
# # def calculateTotal(tom):
# #     total = 0
# #     tom = "mintu.txt"
# #     with open(tom, "r") as f:
# #         lines = f.readlines()
# #         print(lines)
# #         for l in lines:
# #             num = int(l.strip())
# #             total = total + num
# #         print(total)
# #
# # x = "mintu.txt"
# # calculateTotal(x)
# #
# """"
# Count the frequency of each character in a string using list comprehension.
# Input: "hello"
# Output: [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
#
# """
#
# # def frequency(words):
# #     output = [word[::-1] for word in words]
# #     return output
# #
# # string = list("hello")
# # print(frequency(string))
#

# def frequency(words):
#
#     letter = {char: words.count(char) for char in words}
#     output = [(k, v) for k, v in letter.items()]
#     return output
#
#
# string = "hello"
# print(frequency(string))
#
#
