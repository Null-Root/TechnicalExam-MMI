from task_repository import TaskRepository
from task import Task
from datetime import datetime


"""
TaskManager

This is the manager of tasks.
This relies on TaskRepository to fetch the task data
"""
class TaskManager:
    def __init__(self):
        self.taskRepository = TaskRepository()

    def add_new_task(self, new_task: Task):
        self.taskRepository.insert_task(new_task)

    def get_all_task(self, sort_by):
        return self.taskRepository.get_all_task(sort_by)

    def get_task(self, id):
        return self.taskRepository.get_task(id)

    def update_existing_task(self, updated_task: Task):
        return self.taskRepository.update_task(updated_task)

    def delete_existing_task(self, id):
        self.taskRepository.delete_task(id)
    
    def mark_task_as_completed(self, id):
        task = self.taskRepository.get_task(id)
        task.status = "Completed"
        self.taskRepository.update_task(task)