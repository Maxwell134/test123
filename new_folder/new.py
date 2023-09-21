# Conversion functions
def to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

menu = ["1. to miles",
        "2. Miles to kilometers",
        "3. Kilograms to pounds",
        "4. Pounds to kilograms",
        "5. Celsius to Fahrenheit",
        "6. Fahrenheit to Celsius",
        "7. Exit"]

is_choice = True

while is_choice:
    print("\nConversion Menu:".upper())
    for i in range(len(menu)):
        print(menu[i])

    user_choice = input("Enter your choice between (1-7): ")

    if user_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input. Choose a valid option (1-7).")
        continue

    if user_choice == "7":
        print("Exit")
        break

    value = float(input("Enter the value to convert: "))

    if user_choice == "1":
        result = to_miles(value)
        print(f"{value} kilometers is equal to {result} miles.")
    elif user_choice == "2":
        result = miles_to_kilometers(value)
        print(f"{value} miles is equal to {result} kilometers.")
    elif user_choice == "3":
        result = kilograms_to_pounds(value)
        print(f"{value} kilograms is equal to {result} pounds.")
    elif user_choice == "4":
        result = pounds_to_kilograms(value)
        print(f"{value} pounds is equal to {result} kilograms.")
    elif user_choice == "5":
        result = celsius_to_fahrenheit(value)
        print(f"{value} Celsius is equal to {result} Fahrenheit.")
    elif user_choice == "6":
        result = fahrenheit_to_celsius(value)
        print(f"{value} Fahrenheit is equal to {result} Celsius.")
