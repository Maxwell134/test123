class VotingSystem:
    def __init__(self):
        self.candidates = [
            {"name": "Alice", "votes": 0},
            {"name": "Bob", "votes": 0},
            {"name": "Carol", "votes": 0},
        ]

    def display_candidates(self):
        index = 1
        for candidate in self.candidates:
            print(f"{index}: {candidate['name']}")
            index += 1

    def vote_for_candidate(self, candidate_name):
        for candidate in self.candidates:
            if candidate_name.lower() == candidate['name'].lower():
                candidate['votes'] += 10
                print(f"You have voted for {candidate['name']}")
                return True
        return False

    def view_results(self):
        for candidate in self.candidates:
            print(f"{candidate['name']} has: {candidate['votes']} votes")
        winner = max(self.candidates, key=lambda x: x['votes'])
        print(f"Winner of the election is: {winner['name']} with {winner['votes']} votes")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Display Candidates")
            print("2. Vote for a Candidate")
            print("3. View Results")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.display_candidates()
            elif choice == '2':
                candidate_name = input("Enter the candidate's name to vote: ")
                if self.vote_for_candidate(candidate_name):
                    print("Vote recorded.")
                else:
                    print("Invalid candidate name. Please choose a candidate from the list.")
            elif choice == '3':
                self.view_results()
            elif choice == '4':
                print("Exiting")
                break
            else:
                print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.run()
