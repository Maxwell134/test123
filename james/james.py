T = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}

for _ in range(T):
    s = input().strip()
    length = len(s)
    happy = False  # Initialize the happy flag to False

    count_vowels = 0
    for char in s:
        if char in vowels:
            count_vowels += 1
            print(count_vowels, end=" ")
            print(char)
            if count_vowels >= 3:  # Check if we have a substring of length > 2
                happy = True
                break
        else:
            count_vowels = 0

    if happy:
        print("HAPPY")
    else:
        print("SAD")
