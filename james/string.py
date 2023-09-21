# """
# Ask a string from user.
# Ask a character from user.
# Ask new character from user.
#
# Replace character with new character from
# the string entered by user.
#
# hello
# o
# z
#
# hellz
# """
# n = input("Enter string: ")
# c = input("Enter character: ")
# new_c = input("Enter new character: ")
#
# b = n.replace(c, new_c)
#
# print("Updated string:", b)

# joining string

a = ("ok", "This", "Done", "Bye") # works for tuple too
b = "".join(i for i in a)  # works only for string
c = [1,2,3,5,6,7,8]
d = "".join(str(i) for i in c)
print(b)
print(d)

a = "aero plane 23 is good"
is_alphabet = False
is_digit = False

for i in a:
    if i.isaplha():
        is_alphabet = True
    elif i.isdigit():
        is_digit = True

if is_alphabet == True and is_digit == True:
    print("Exists")
else:
    print("Does not Exists")