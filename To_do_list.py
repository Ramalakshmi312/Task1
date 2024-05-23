class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = False
        print(f"Task '{task}' added.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for task, completed in self.tasks.items():
                status = "completed" if completed else "not completed"
                print(f"Task: {task} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to mark as completed: ")
            todo_list.complete_task(task)
        elif choice == '3':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
