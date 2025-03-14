from datetime import datetime
from task import Task
from task_manager import TaskManager
from util_input import ValidatedInput
from declared_enums import PRIORITY, STATUS
import os

"""
UserInterface

This is used for the display in the commandline
This is where user interacts with the application
"""
class UserInterface(ValidatedInput):
    def __init__(self):
        self.task_manager = TaskManager()
    
    def _display_tasks(self):
        tasks = self.task_manager.get_all_task("status")
        for task in tasks:
            print(f"Task -> {task.title}, \n ID -> ({task.task_id})")
        print("\n")

    def start(self):
        print("Task Management")
        print("=============================")
        print("[a] Add New Task")
        print("[b] Read All Tasks")
        print("[c] Update Existing Task")
        print("[d] Delete Existing Task")
        print("[e] Mark task as completed")
        print("=============================")

        choice = input("Choice?: ")
        if choice.strip() == "":
            print("No choice selected!")
            return

        if choice == "a":
            title = self.get_string("Title", "Untitled")
            description = self.get_string("Description", "No Desc")
            due_date = self.get_date("Due Date")
            priority_level = self.get_selected_item("Priority Level", PRIORITY, PRIORITY[0])
            status = self.get_selected_item("Status", STATUS, STATUS[0])
            
            newTask = Task("", title, description, due_date, priority_level, status, datetime.today())

            self.task_manager.add_new_task(newTask)

        elif choice == "b":
            sort_by = self.get_selected_item("Sort by", ["due_date", "priority_level", "status"], "status")
            print(f"Sorting by: {sort_by}")
            tasks = self.task_manager.get_all_task(sort_by)
            print("\n")
            for task in tasks:
                print(f"Task -> {task.title}, \n ({task.task_id})")
                print(f"Description    : {task.description}")
                print(f"Due Date      : {task.due_date}")
                print(f"Priority      : {task.priority_level}")
                print(f"Status        : {task.status}")
                print("\n")


        elif choice == "c":
            self._display_tasks()

            task_id = self.get_string("Task ID", "")

            # Fetch Task
            task = self.task_manager.get_task(task_id)
            if task:
                print(f"Task -> {task.title}, ID: -> {task.task_id}")

                task.title = self.get_string("Title", task.title)
                task.description = self.get_string("Description", task.description)
                task.due_date = self.get_date("Due Date", task.due_date)
                task.priority_level = self.get_selected_item("Priority Level", PRIORITY, task.priority_level)
                task.status = self.get_selected_item("Status", STATUS, task.status)

                self.task_manager.update_existing_task(task)

            else:
                print("Invalid ID")

        elif choice == "d":
            self._display_tasks()

            task_id = self.get_string("Task ID", "")

            # Fetch Task
            task = self.task_manager.get_task(task_id)

            if task:
                print(f"Task -> {task.title}, ID: -> {task.task_id}")
                
                confirm_choice = input("Confirm? (Y/n)")
                if confirm_choice.lower() == 'y':
                    self.task_manager.delete_existing_task(task_id)
                else:
                    print("Action Cancelled")
            else:
                print("Invalid ID")

        elif choice == "e":
            self._display_tasks()

            task_id = self.get_string("Task ID", "")

            # Fetch Task
            task = self.task_manager.get_task(task_id)

            if task:
                print(f"Task -> {task.title}, ID: -> {task.task_id}")
                self.task_manager.mark_task_as_completed(task_id)
            else:
                print("Invalid ID")

        print("\n\nAction Executed!")


userInterface = UserInterface()
while True:
    os.system("cls")
    userInterface.start()

    exit_choice = input('Exit (Y/n)')
    if exit_choice.lower() == "y":
        break