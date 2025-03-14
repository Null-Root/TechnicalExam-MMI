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
        self.task_repository = TaskRepository()

    """
    This adds a new task
    """
    def add_new_task(self, new_task: Task):
        self.task_repository.insert_task(new_task)

    """
    This retrieves all task and sorts it by sort_by
    """
    def get_all_task(self, sort_by):
        return self.task_repository.get_all_task(sort_by)

    """
    This retrieve a task using an id
    """
    def get_task(self, id):
        return self.task_repository.get_task(id)

    """
    This updates an existing task
    """
    def update_existing_task(self, updated_task: Task):
        return self.task_repository.update_task(updated_task)

    """
    This delete an existing task using an id
    """
    def delete_existing_task(self, id):
        self.task_repository.delete_task(id)
    
    """
    This mark the task as completed
    """
    def mark_task_as_completed(self, id):
        task = self.task_repository.get_task(id)
        task.status = "Completed"
        self.task_repository.update_task(task)