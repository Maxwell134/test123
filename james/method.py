# # a = {
# #     "name": "Anirudh Khurana",
# #     "age": 33,
# #     "gender": "Male",
# #     "m1": 55,
# #     "m2": 99,
# #     "m3": 88,
# # }
# #
# # # for k in a.keys():
# # #     print(f"{k} - {a[k]}")
# #
# # # for v in a.values():
# # #     print(v)
# #
# # # for item in a.items():
# # #     print(f"{item[0]} -> {item[1]}")
# #
# #
# # for k, v in a.items():
# #     print(k, v)
# # a = {
# #     "name": "Anirudh Khurana",
# #     "age": 33,
# #     "gender": "Male",
# #     "m1": 55,
# #     "m2": 99,
# #     "m3": 88,
# # }
# #
# # # for k in a.keys():
# # #     print(f"{k} - {a[k]}")
# #
# # # for v in a.values():
# # #     print(v)
# #
# # # for item in a.items():
# # #     print(f"{item[0]} -> {item[1]}")
# #
# #
# # for k, v in a.items():
# #     print(k, v)
# #
# # my_dict = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}
# #
# # value = int(input("Enter value = "))
# #
# # for k, v in my_dict.items():
# #     if v == value:
# #         print(k)
#
# a = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}
# #
# # y = a.get('m4')
# # print(y)
# key = input("Enter the key: ")
# result = a.get(key)
#
# if result == None:
#     print("key not found")
# else:
#     print(result)
#
# # print(str(a))
# # print(str(a)[0])
# # print(list(str(a)))
#
# # print(a.values())
# # print(type(a.values()))
# # print(list(a.keys()))
# # print(list(a.values()))

# my_dict = {"m1": 67, "m2": 11, "m3": 78, "m4": 31, "m5": 17, "m6": 62, "m7": 7}
#
# for key, value in my_dict.items():
#     if value < 33:
#         print(key)
#
#         a = {
#             "Anirudh": [34, 15, 74, 88, 11],
#             "Sanjay": [75, 12, 11, 89, 77],
#             "Akul": [73, 99, 90, 91, 11],
#             "Nihar": [55, 43, 19, 83],
#             "Karan": [77, 84, 21, 22, 20],
#         }

"""
        Anirudh has scored 444 marks
        Sanjay has scored 444 marks
        Akul has scored 444 marks
        Nihar has scored 444 marks

        MEthod 1 - With using SUM()
        MEthod 2 - Without using SUM()
"""

a = {
            "Anirudh": [34, 15, 74, 88, 11],
            "Sanjay": [75, 12, 11, 89, 77],
            "Akul": [73, 99, 90, 91, 11],
            "Nihar": [55, 43, 19, 83],
            "Karan": [77, 84, 21, 22, 20],
        }
# for key, value in a.items():
#         sum1 = sum(value)
#         a[key] = sum1
# print(a)


# for key, value in a.items():
#     sum = 0
#     for i in value:
#         sum += i
#         a[key] = sum
# print(a)
# maximum = 0
#
# for key, value in a.items():
#     if value > maximum:
#         maximum = value
#         student = key
#
# print(f"{student}, {maximum}")

# student = {}
# for _ in range(0, 3):
#     name = input("Enter name: ")
#     marks = []
#     for _ in range(0, 5):
#         m = int(input("Enter marks: "))
#         marks.append(m)
#
#     student[name] = marks
#
# print(student)

details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
    },
    "Sagar": {
        "age": 11,
        "city": "Delhi",
        "phone": 985474587,
    },
    "Muskan": {
        "age": 16,
        "city": "Agra",
        "phone": 8585747474,
    },
}

for k, v in details.items():
    age = v["age"]
    print(f"{k} has age of {age}")

for k, v in details.items():
    print(f"Name = {k}")
    print(f"Age = {v['age']}")
    print(f"City = {v['city']}")
    print(f"Phone = {v['phone']}\n")


for k, v in details.items():
    print(f"Name = {k}")
    print(f"City = {v['city']}")
    print(f"Phone = {v['phone']}")
    age = v.get("age")  # 16 / None
    if age:
        print(age)
    else:
        print("Age does not exists")



