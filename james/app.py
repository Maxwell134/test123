# # # # x,y,z = map(float, input("Enter number").split())
# # # # print(x)
# # # # print(y)
# # # # print(z)
# # # """
# # # Write a python program to ask a string from user. Then count the number of
# # # vowels and number of consonants in that string.
# # # """
# # #
# # # n = input("Enter the string: ").lower()
# # #
# # # vowels = ('a', 'e', 'i', 'o', 'u')
# # # consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
# # #
# # # count_vowel = 0
# # # count_consonant = 0
# # #
# # # for char in n:
# # #     if char in vowels:
# # #         count_vowel += 1
# # #     elif char in consonants:
# # #         count_consonant += 1
# # #
# # # print(f"Count of vowels: {count_vowel}")
# # # print(f"Count of consonants: {count_consonant}")
# # """
# # # Ask a string from user.
# # # Print the string with first 2 letters and last 2 letters.
# # Example string: aeroplane
# # Output: aene
# # """
# # n = input("Enter the string: ").lower()
# # output = n[:2] + n[-2:]
# # print(output)
# #
# # Write a python program to only print the second half of the string. Ask string from user.
# n = input("Enter the string: ").lower()
# # print(len(n))
# output = n[-(len(n)//2):]
# print(output)
# Write a Python program to check if a string is empty or not.
while True:
    n = input("Enter the string: ").lower()
    if len(n) != 0:
        print("String not empty")
    else:
        print("String is empty ")
        break














