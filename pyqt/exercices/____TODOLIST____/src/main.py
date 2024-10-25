from todolist.managers.todolist_manager import TodoListManager
from todolist.persistence.csv_persistence import CsvPersistence


class TodoListViewCLI():
    def __init__(self, manager):
        self.manager = manager

    def display_todo_list(self, tasks):
        for index, task in enumerate(tasks):
            status = "Done" if task.is_done else "Not Done"
            print(f"{index + 1}. {task.name} - {status}")

    def mark_task_as_done(self, index):
        print(f"Task {index + 1} marked as done.")

    def show(self):
        self.interaction_loop()

    def interaction_loop(self):
        """
        Main CLI interaction loop to interact with the user.
        """
        self.manager.load()

        while True:
            print("\nOptions:")
            print("1. Add a task")
            print("2. Update task")
            print("3. Mark a task as done")
            print("4. Delete task")
            print("5. Save tasks")
            print("6. Load tasks")
            print("7. Exit")

            option = input("Choose an option (1-7): ")

            match option:
                case "1":
                    task_description = input("Enter task description: ")
                    self.manager.add_task(task_description)
                case "2":
                    index = int(input("Enter task index to update: ")) - 1
                    task_description = input("Enter task description: ")
                    self.manager.update_task(index, task_description)
                case "3":
                    index = int(input("Enter task index to mark as done: ")) - 1
                    self.manager.mark_task_as_done(index)
                case "4":
                    index = int(input("Enter task index to delete: ")) - 1
                    self.manager.delete_task(index)
                case "5":
                    self.manager.save()
                case "6":
                    self.manager.load()
                case "7":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option. Please choose again.")
                    
            self.display_todo_list(self.manager.todo_list.tasks)

def main():
    FILE_NAME = "data/tasks.csv"

    # Set up persistence (CsvPersistence in this case)
    persistence = CsvPersistence(FILE_NAME)

    # Create the TodoListManager, responsible for the model and persistence
    manager = TodoListManager(persistence)
    view = TodoListViewCLI(manager)
    view.show()
  
if __name__ == "__main__":
    main()