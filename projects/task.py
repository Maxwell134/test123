from datetime import date


class TaskManager:

    def __init__(self):
        self.task_manager = {}

    def create_task(self):
        task_id = int(input("Enter the task ID: "))
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        deadline_str = input("Enter the deadline (YYYY-MM-DD): ")

        try:
            deadline = date.fromisoformat(deadline_str)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        if task_id in self.task_manager:
            print(f"Task ID {task_id} already exists.")
        else:
            self.task_manager[task_id] = {
                "title": title,
                "description": description,
                "deadline": deadline
            }
            print(f"Task ID {task_id} created successfully.")

    def view_task(self):
        task_id = int(input("Enter the task ID to view: "))
        if task_id in self.task_manager:
            task = self.task_manager[task_id]

            print("\nTask Details:")
            print(f"Task ID: {task_id}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Deadline: {task['deadline']} ")
        else:
            print(f"Task ID {task_id} does not exist.")

task_manager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Create a Task")
    print("2. View a Task")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_manager.create_task()
    elif choice == "2":
        task_manager.view_task()
    elif choice == "3":
        print("Thank you for visiting us.")
        break
    else:
        print("Invalid choice.")
