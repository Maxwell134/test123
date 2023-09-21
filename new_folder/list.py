candidates = [{"name": "Alice", "votes": 0},
              {"name": "Bob", "votes": 0},
              {"name": "Carol", "votes": 0}]

def display_candidates():
    index = 1
    for candidate in candidates:
        print(f"{index}: {candidate['name']}")
        index += 1


def vote_for_candidate(candidate_name):


    for candidate in candidates:
        if candidate['name'].lower() == candidate_name.lower():
            candidate['votes'] += 10
            print(f"Thank you for voting for {candidate['name']}.")
            return True

    print("No candidates available.")


def view_result():

    for candidate in candidates:
        print(f"candidate {candidate['name']} has {candidate['votes']}")



    winner = max(candidates, key=lambda x: x['votes'])
    print(f"Winner of the election {winner['name']} has {winner['votes']}")

while True:
    print("\nMenu:")
    print("1. Display Candidates")
    print("2. Vote for a Candidate")
    print("3. View Results")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_result()

    elif choice == "2":

        candidate_name = input("Enter the candidate's name to vote: ")
        if vote_for_candidate(candidate_name):
            print("Vote recorded  securely")


    elif choice == "3":
        view_result()

    elif choice == "4":
        break
    else:
        print("Invalid choice")



display_candidates()








