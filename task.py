from datetime import datetime


"""
Task

This will serve as the model for a "task"
"""
class Task:
    def __init__(
        self,
        task_id: str,
        title: str,
        description: str,
        due_date: str,  # Stored as ISO date string (YYYY-MM-DD)
        priority_level: str,
        status: str,
        creation_ts: str  # ISO timestamp
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority_level = priority_level
        self.status = status
        self.creation_ts = creation_ts
