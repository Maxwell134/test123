import string

def is_strong_pass(password):

    def has_minimum_length(password):
        return len(password)

    def has_upper(password):
        return any(char.isupper() for char in password)

    def has_lower(password):
        return any(char.islower() for char in password)

    def has_numeric(password):
        return any(char.isnumeric() for char in password)

    def has_special_character(password):
        special_chars = string.punctuation
        return any(char in special_chars for char in password)

    criteria_met = sum(
        [has_lower(password), has_numeric(password), has_upper(password), has_special_character(password)])

    if criteria_met == 4 and has_minimum_length(password) >= 8:
        return "Strong: All criteria met"

    elif criteria_met >= 3 and len(password) >= 8:
        return "Moderate: 3 criteria met"
    else:
        return "Weak: 1-2 criteria met"


print("Welcome to password checker Follow the instruction\n")

instruction = [

    "a. Minimum length of 8 characters.",
    "b. Presence of at least one uppercase letter",
    "c. Presence of at least one lowercase letter",
    "d. Presence of at least one number",
    "e. Presence of at least one special character (e.g., !@#$%^&*)"

]

for i in range(len(instruction)):
    print(instruction[i])

while True:
    user_input = input("Enter 2 to enter password or enter 1 to exit: ")
    if user_input == "1":
        break

    elif user_input == "2":
        user_input = input("Enter the password:  ")

    else:
        print("Invalid choice . choose 1 or 2 ")
        continue

    is_strong_pass(user_input)
    print(is_strong_pass(user_input))