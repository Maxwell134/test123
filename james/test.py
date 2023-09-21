# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     a = list(map(int, input().split()))
#
#     most_common_element = None
#     most_common_count = 0
#     for num in a:
#         count = a.count(num)
#         if count > most_common_count:
#             most_common_element = num
#             most_common_count = count
#
#     non_equal_count = 0
#     for num in a:
#         if num != most_common_element:
#             non_equal_count += 1
#
#     pairs_needed = non_equal_count
#     print(pairs_needed)

# for _ in range(0, int(input())):
#     length = int(input())
#     numbers = list(map(int, input().split()))
#
#     max_freq_number = numbers[0]
#     max_freq = numbers.count(numbers[0])
#     for i in set(numbers):
#         r = numbers.count(i)
#         if r > max_freq:
#             max_freq = r
#             max_freq_number = i
#
#     count = 0
#     for i in numbers:
#         if i != max_freq_number:
#             count += 1
#     print(count)

details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
        "marks": [11, 22, 33, 44, 55],
    },
    "Sagar": {
        "age": 11,
        "city": "Delhi",
        "phone": 985474587,
        "marks": [65, 12, 76, 88, 33],
    },
    "Muskan": {
        "age": 16,
        "city": "Agra",
        "phone": 8585747474,
        "marks": [98, 21, 54, 73, 88],
    },
}

# Input new details
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
phone = int(input("Enter phone: "))
marks = list(map(int, input("Enter marks (space-separated): ").split()))

# Update the details dictionary
details[name] = {
    "age": age,
    "city": city,
    "phone": phone,
    "marks": marks,
}

print("details:", details)


