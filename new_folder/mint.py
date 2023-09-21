def questionnaire(questions, choices, correct_answers):
    while True:
        print("Welcome to Quiz board. Each quiz contains 1 mark each.")
        print("Please enter 1 to continue or 2 to exit.")
        input_choice = input("Enter 1 or 2 to exit: ")

        if input_choice == "2":
            print("We are sad to let you go. Please visit us again.")
            break
        elif input_choice != "1":
            print("Invalid choice!\n")
            continue
        else:

            score = 0
            for i in range(len(questions)):
                print(f"Question {i + 1}: {questions[i]}")

                for choice in choices[i]:
                    print(choice)

                user_choice = input("Enter your choice: A/B/C/D: ").strip().upper()

                if user_choice == correct_answers[i]:
                    score += 1
                    print("Correct!\n")
                else:
                    print("Incorrect!\n")

        print(f"Score obtained is {score}")

        if score >= 4:
            print("Excellent work")
        elif score >= 3:
            print("Good job")
        else:
            print("You need to try harder")


        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break


questions = [
    "What is the capital of France?",
    "Which planet is known as the 'Red Planet'?",
    "What is the largest mammal in the world?",
    "Which of the following is a prime number?",
    "Which unit of the computer is considered as the brain of the computer?"
]

choices = [
    ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
    ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
    ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Lion"],
    ["A. 15", "B. 23", "C. 21", "D. 27"],
    ["A. Memory Unit", "B. Input Unit", "C. CPU", "D. Output Input"]
]

correct_answers = ["A", "B", "C", "B", "C"]

# Call the questionnaire function to start the quiz
questionnaire(questions, choices, correct_answers)
