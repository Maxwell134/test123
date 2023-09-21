# # # # # numbers = [4, 5, 6, 8, 9]
# # # # # product = 1
# # # # #
# # # # # for i in numbers:
# # # # #     if numbers.count(i) == 1:
# # # # #         product *= i
# # # # #     else:
# # # # #         product = 0
# # # # #
# # # # # print(product)
# # # #
# # # # a = {
# # # #
# # # #     "science": 78,
# # # #     "maths": 99,
# # # #     "english": 78,
# # # #     "csc": 70
# # # # }
# # # # total = 0
# # # # for value in a.values():
# # # #     total += value
# # # # print(total)
# # # # total = 0
# # # #
# # # # total = 0
# # # # for key, value in a.items():
# # # #     print("Subject:", key, "- Score:", value)
# # # #     total += value
# # # #
# # # # print("Total:", total)
# # #
# # #
# # # # Write a Python program to generate and
# # # # print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # #
# # # new = {}
# # # n = 6
# # # for i in range(1, 6):
# # #     key = i
# # #     value = i**2
# # #     new[key] = value
# # #
# # # print(new)
# #
# # # Write a Python program to check if a dictionary is empty or not.
# #
# # my_list = {
# #
# # }
# #
# # if len(my_list) == 0:
# #     print("Empty")
# # else:
# #     print("Exist")
# """
# Q3. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
#
# """
#
#
# # for key in d1:
# #     if key in d2:
# #         d1[key] += d2[key]
# #
# # new = {}
# # for key in d1:
# #     new[key] = d1[key]
# #
# # for key in d2:
# #     if key not in new:
# #         new[key] = d2[key]
# #
# # print(new)
#
# #
# # d1 = {'a': 100, 'b': 200, 'c': 300}
# # d2 = {'a': 300, 'b': 200, 'd': 400}
# #
# # for key in d1:
# #     if key in d2:
# #         d1[key] += d2[key]
# #
# # for key in d2:
# #     if key not in d1:
# #         d1[key] = d2[key]
# # print(d1)
# """
# Write a Python program to remove duplicates from Dictionary.
# Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7:60, 8:50}
# Output: {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10}
#
# """
#
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
#
# new = {}
#
# for key in d1:
#     if key in d2:
#         d1[key] += d2[key]
#
# for key in d2:
#     if key not in d1:
#         d1.update(d2)
# print(d1)
#
#  = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
# b = {}
#
# for k, v in a.items():
#     if v not in b.values():
#         b[k] = v
#
# print(b)
#
a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 11],
    "Karan": [77, 84, 21, 22, 20],
}

"""
Anirudh has scored 444 marks
Sanjay has scored 444 marks
Akul has scored 444 marks
Nihar has scored 444 marks

MEthod 1 - With using SUM()
MEthod 2 - Without using SUM()

"""

# Method 1
sums ={}
for key, value in a.items():
    sum = 0
    for i in value:
        sum += i
        sums[key] = sum
    print(f"{key} has scored {sum}")
print(sums)
# Method 2

i = 0
while i < 10:
    print(i)
    i += 1



