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

    def add_new_task(
        self,
        title,
        description,
        due_date,
        priority_level,
        status
    ):
        newTask = Task("", title, description, due_date, priority_level, status, datetime.today())
        self.taskRepository.insert_task(newTask)

    def get_all_task(self, sort_by):
        return self.taskRepository.get_all_task(sort_by)

    def get_task(self, id):
        return self.taskRepository.get_task(id)

    def update_existing_task(self, task_id, title, description, due_date, priority_level, status, creation_ts):
        existingTask = Task(task_id, title, description, due_date, priority_level, status, creation_ts)
        return self.taskRepository.update_task(existingTask)

    def delete_existing_task(self, id):
        self.taskRepository.delete_task(id)
    
    def mark_task_as_completed(self, id):
        task = self.taskRepository.get_task(id)
        task.status = "Completed"
        self.taskRepository.update_task(task)