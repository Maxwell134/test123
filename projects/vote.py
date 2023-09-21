
class VoteSystem:

    def __init__(self):

        self.candidates = [{"name": "Alice", "votes": 0},
              {"name": "Bob", "votes": 0},
              {"name": "Carol", "votes": 0}]


    def add_candidate(self):

        candidate_id = input("Enter the candidate name: ")

        for candidate in self.candidates:

            if candidate['name'].lower() == candidate_id.lower():

                candidate['votes'] += 10
                print(f"Thank you for voting for {candidate['name']}.")
                break
        else:

            print(f"{candidate_id} does not exist")

    def view_candidate(self):

        for candidate in self.candidates:

            if candidate:

                print(f"{candidate['name']} has {candidate['votes']}")

        print(self.candidates)

    def view_result(self):
        max_votes = 0
        winner = None
        is_draw = False

            # Check if there are any candidates with the same number of votes

        for candidate in self.candidates:
            if candidate['votes'] > max_votes:
                max_votes = candidate['votes']
                winner = candidate['name']

            elif candidate['votes'] == max_votes:
                is_draw = True


        if is_draw:

            print("No Winner for the Election")

        elif winner:
            print(f"{winner} has {max_votes} Maximum votes")



            # elif candidate['votes'] == max_votes:



        # winner = max(self.candidates, key= lambda x: x['votes'])
        # print(f"Winner of the election {winner['name']} has {winner['votes']}")


vote_system = VoteSystem()

while True:
    print("\nMenu:")
    print("1. Display Candidates")
    print("2. Vote for a Candidate")
    print("3. View Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vote_system.view_candidate()

    elif choice == "2":
        vote_system.add_candidate()

    elif choice == "3":
        vote_system.view_result()

    elif choice == "4":
        break

    else:

        print(f"Invalid choice")














































