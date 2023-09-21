from random import choice

fruits = ["Apple", "Banana", "Orange", "Strawberry", "Blueberry", "Grape",
          "Mango", "Watermelon",
          "Pineapple", "Kiwi", "Peach", "Pear", "Cherry",
          "Raspberry",
          "Lemon", "Lime", "Grapefruit",
          "Papaya", "Avocado", "Plum"]

def hangman():
    while True:
        guess_word = ""
        guess_list = []
        attempts = 5
        chosen_fruit = choice(fruits).lower()
        print(chosen_fruit)

        for _ in chosen_fruit:
            guess_list.append("_")
        # print(guess_list)

        while attempts > 0:
            user_guess_letter = input("Enter a letter: ").lower()

            for index in range(len(chosen_fruit)):
                if chosen_fruit[index] == user_guess_letter:
                    guess_list[index] = user_guess_letter

            print(f"Guess letter is: {guess_word.join(guess_list)}")

            if user_guess_letter not in chosen_fruit:
                attempts -= 1
                print("Attempts remaining:", attempts)

            if "_" not in guess_list:
                print("Congratulations! You guessed the word:", chosen_fruit)
                break

        if attempts <= 0:
            print("Sorry, you ran out of attempts. The word was:", chosen_fruit)


        user_input = input("Would you like to play again? (yes/no): ").lower()
        if user_input == "yes":
            continue
        else:
            print("Thank you for playing Hangman!")
            break

hangman()






