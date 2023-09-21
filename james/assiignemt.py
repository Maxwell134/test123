# # T = int(input(" Enter case: "))
# #
# # max = 0
# # points = 0
# # # count1 = 0
# # # count2 = 0
# # winner = 0
# # new = []
# # for _ in range(T):
# #     x, y = map(int, input("Enter number:  ").split())
# #     points = abs(x -y)
# #
# #     new.append(points)
# # for i in new:
# #     if i > max:
# #         max = i
# # print(max, winner)
# # # print(count1)
# # # print(count2)
# #
#
# # from timeit import timeit
# # def generateList():
# #     a = []
# #     for i in range(1, 1000):
# #         a.append(i)
# #     return a
# #
# #
# # def generateList2():
# #     return [i for i in range(1, 1000)]
# #
# #
# # t1 = timeit(stmt=generateList)
# # t2 = timeit(stmt=generateList2)
# #
# # print(t1)
# # print(t2)
#
# # a = [i for i in range(1, 100) if i % 2 == 0 and i % 3 == 0]
# # print(a)
#
# # def checkPrime(num) -> bool:
# #     factors = 0
# #     for i in range(1, num + 1):
# #         if num % i == 0:
# #             factors += 1
# #     if factors == 2:
# #         return True
# #     return False
# #
# #
# # # a = [i for i in range(1, 31) if checkPrime(i) == True]
# # a = [i for i in range(1, 31) if checkPrime(i)]
# #
# # print(a)
#
# # lambda
#
# # def add(num1, num2):
# #     #...
# #     return num1 + num2
#
# # Lambda/Anonymous function
# # add = lambda x, y: x + y
# # generateEvenList = lambda start, end: [i for i in range(start, end + 1) if i % 2 == 0]
# #
# # print(add(10, 20))
# # print(generateEvenList(4, 20))
# #
# # #
# # x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # print(x.items())
# # r = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
# # print(r)
#
# """
# Q4. Write a Python function flatten_list(nested_list) that takes a
# nested list as input and returns a flattened version of the list.
#
#             new.append(i)
#     return new
#
# nested_list_1 = [1, [2, 3, [4, 5]], 6, [7, 8]]
# nested_list_2 = [1, [2, [3, [4, [5]]]]]
# nested_list_3 = [1, 2, 3, 4, 5]
#
# print(flatten_list(nested_list_1))
# print(flatten_list(nested_list_2))
# print(flatten_list(nested_list_3))
#
# """
# cities = [
# {"city": "Paris", "country": "France"},
# {"city": "Berlin", "country": "Germany"},
# {"city": "Geneva", "country": "Switzerland"},
# {"city": "Nice", "country": "France"},
# {"city": "Rome", "country": "Italy"},
# {"city": "Dubai", "country": "UAE"},
# {"city": "Bangkok", "country": "Thailand"},
# {"city": "Phuket", "country": "Thailand"},
# {"city": "Tokyo", "country": "Japan"},
# {"city": "Osaka", "country": "Japan"}]
#
# # new = []
# # for key in cities:
# #     new.append(key['country'])
# # new = [key['country'] for key in cities]
# #
# # out = {}
# # for i in new:
# #     y = new.count(i)
# #     out[i] = y
# # print(out)
#
#
# cities = [
#     {"city": "Paris", "country": "France"},
#     {"city": "Berlin", "country": "Germany"},
#     {"city": "Geneva", "country": "Switzerland"},
#     {"city": "Nice", "country": "France"},
#     {"city": "Rome", "country": "Italy"},
#     {"city": "Dubai", "country": "UAE"},
#     {"city": "Bangkok", "country": "Thailand"},
#     {"city": "Phuket", "country": "Thailand"},
#     {"city": "Tokyo", "country": "Japan"},
#     {"city": "Osaka", "country": "Japan"},]
#
#
# countries = [x['country'] for x in cities]
#
# new = [city['country'] for city in cities]
#
# # out = []
# # for country in new:
# #     count = new.count(country)
# #     out.append({'country': country, 'number_of_cities': count})
#
# out = [{'country': country, 'number_of_cities': new.count(country)} for country in new]
#
# print(set(countries))
# print(out)
#

""""
Create a python if-else program to check if the given numbers are greater or not, also
check whether the given number is a prime number or not. Make use of python if-else,
and elif statements for the same.

"""

# a = list(map(int, input("Enter number: ").split()))
# maxi = 0
#
# for i in range(len(a)):
#     if a[i] > maxi:
#         maxi = a[i]

def add(a,b):
    return a + b

def sub(a, b):
    return a - b


