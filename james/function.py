# # # # def removeDuplicates(my_list: list[int]):
# # # #     new = []
# # # #
# # # #     for i in my_list:
# # # #         if i not in new:
# # # #             new.append(i)
# # # #
# # # #     return new
# # # #
# # # #
# # # # input_list = [2, 3, 5, 4, 5, 6, 2, 4, 6]
# # # # result = removeDuplicates(input_list)
# # # # print(result)
# # #
# # # students = [
# # #     {
# # #         "name": "Anirudh",
# # #         "marks": 89,
# # #     },
# # #     {
# # #         "name": "Sagar",
# # #         "marks": 11,
# # #     },
# # #     {
# # #         "name": "Sanjay",
# # #         "marks": 6,
# # #     },
# # #     {
# # #         "name": "Vandana",
# # #         "marks": 56,
# # #     },
# # # ]
# # #
# # # new = {}
# # # highest_marks = 0
# # # for student in students:
# # #
# # #     if student['marks'] > highest_marks:
# # #         highest_marks = student['marks']
# # #         new = student
# # # print(highest_marks)
# # # print(new)
# #
# # """
# # Write a Python program to convert more than one list to a nested dictionary.
# #
# # Example 1
# #
# #
# # Output = [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
# # """
# #
# # student_id = ["S001", "S002", "S003", "S004"]
# # student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
# # student_grade = [85, 98, 89, 92]
# # student_dict = {}
# # output = []
# #
# # # Iterate through the lists and create the nested dictionary
# # for i in range(len(student_id)):
# #     student_dict = {student_id[i]: {student_name[i]: student_grade[i]}}
# #     output.append(student_dict)
# #
# # print(output)
#
# """
# Make your own dictionary, sort the dictionary by values.
#
# Example 1
# data = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}
# Output = {'grape': 1, 'banana': 2, 'apple': 5, 'orange': 8}
# """
# # data = {"English": 5, "Maths": 2, "Science": 14}
# #
# # list =[]
# # for k, v in data.items():
# #     list.append(v)
# #
# # list.sort()
# #
# # Output = {}
# # for i in list:
# #     for key, value in data.items():
# #         if value == i:
# #             Output[key] = value
# #
# # print(Output)
#
# # data = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}
# #
# # out = {}
# # sorted_values = sorted(data.values())
# #
# # for value in sorted_values:
# #     for key, values in data.items():
# #         if data[key] == value:
# #             out[key] = data[key]
# # print(out)
#
# """
# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Make list on your own.
#
# Example 1
# colors = [("green", 1), ("purple", 2), ("orange", 3), ("green", 4), ("blue", 1)]
# Output = {'green': [1, 4], 'purple': [2], 'orange': [3], 'blue': [1]}
# """
# colors = [("green", 1), ("purple", 2), ("orange", 3), ("green", 4), ("blue", 1)]
#
# output = {}
#
# for color, value in colors:
#     if color in output:
#         output[color].append(value)
#     else:
#         output[color] = [value]
#
# print(output)

"""
Make a dictionary on your own, with mixed key values.
(Key can be any data type and value can be any data type).
Then ask a value (K) from the user.
Remove all the keys from the dictionary having values greater than K.

"""
test_dict = {"Anirudh": "Male", "xyz": 8, "Sagar": "1111", "Pqr": 2, "ABBC": 9}

# new_dict = {}
#
# for key, value in test_dict.items():
#     if str(value) <= str(6) or isinstance(value, str):
#         new_dict[key] = value
#
# print(new_dict)

"""
Write a Python function is_palindrome(s) that takes a string s as input and returns True 
if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

"""
# def palindrome(s):
#
#     if s == s[::-1]:
#         return True
#     return False
#
# x = input("Enter the string: ")
# print(palindrome(x))

# """
# Write a Python function word_count(sentence) that takes a sentence as input and
# returns a dictionary where keys are words and
# values are the counts of those words in the sentence.
# """
# def word_count(sentence):
#     string = sentence.split()
#     dic = {}
#     for words in string:
#         count = string.count(words)
#         dic[words] = count
#
#     return dic
#
# new = input("Enter sentence: ")
# print(word_count(new))

# x = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
#
# dic = {}
#
# for words in x:
#     count = x.count(words)
#     dic[words] = count
# print(dic)
"""
Write a Python function flatten_list(nested_list) that takes a 
nested list as input and returns a flattened version of the list.

"""
#
# def flatten_list(nested_list):
#     new = []
#     for i in nested_list:
#         if type(i) == list:
#             flatten_list(i)
#         else:
#             new.append(i)
#     return new
#
#
# my_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
# flattened = flatten_list(my_list)
# print(flattened)

# flat_list = []
# arr = [1, [2, [3, [4, [5]]]]]
# def flatten_list(nested_list):
#
#     for i in nested_list:
#         if type(i) == list:
#             flatten_list(i)
#         else:
#             flat_list.append(i)
#
#     return flat_list
#
# print(flatten_list(arr))


"""
Q6. Write a Python program to convert a dictionary into a list of lists.

Example 1
data = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
output = [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
"""
#
# data = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# out = []
#
# for key, value in data.items():
#     out.append([key, value])
# print(out)
"""
Q7. Write a Python program to filter even numbers from a dictionary of values.

Example 1
data = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
output = {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

"""
# data = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
#
#
# output = {}
# for key, value in data.items():
#     new = []
#     for even in value:
#         if even % 2 == 0:
#            new.append(even)
#     output[key] = new
#
# print(output)
"""
Q8. Write a Python program to find the shortest list of values for the keys in a given dictionary.

output = ['VI', 'VIII', 'X']

"""
# data = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
#
# new = []
# for key, value in data.items():
#
#     count = 0
#     for i in value:
#         count += 1
#     if count == 1:
#         new.append(key)
# print(new)









