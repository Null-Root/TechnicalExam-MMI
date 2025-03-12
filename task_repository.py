from task import Task
import pymongo


"""
TaskRepository

This is the intermediary between the MongoDB and TaskManager
This handles all MongoDB related operations
"""
class TaskRepository:
    def get_collection(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["task_db"]
        mycol = mydb["task_collection"]
        return mycol

    def insert_task(self, task: Task):
        collection = self.get_collection()
        
        task_dict = task.__dict__
        insert_res = collection.insert_one(task_dict)

        # Re-fetch the inserted document
        fetch_res = collection.find_one({"_id": insert_res.inserted_id})

        collection.update_one(
            {"_id": insert_res.inserted_id}, 
            {"$set": {"task_id": str(fetch_res["_id"])}}
        )
    
    def get_all_task(self, sortBy):
        collection = self.get_collection()
        cursor = collection.find().sort(sortBy)
        tasks = [Task(**{k: v for k, v in doc.items() if k != "_id"}) for doc in cursor]
        return tasks

    def get_task(self, task_id):
        collection = self.get_collection()
        
        # Find the document using task_id
        fetch_res = collection.find_one({"task_id": task_id})
        
        if fetch_res:
            return Task(**{k: v for k, v in fetch_res.items() if k != "_id"})  # Exclude _id
        return None  # Return None if no task found
    
    def update_task(self, task: Task):
        collection = self.get_collection()

        # Convert Task object to dictionary and remove _id
        task_dict = task.__dict__.copy()
        task_id = task_dict.pop("task_id", None)  # Extract task_id and remove from dict
        task_dict.pop("creation_ts")

        if not task_id:
            return False  # No task_id, cannot update

        # Update the task with the given task_id
        update_res = collection.update_one(
            {"task_id": task_id},
            {"$set": task_dict}  # Update with all fields from Task object
        )

        return update_res.modified_count > 0  # Returns True if update was successful


    def delete_task(self, task_id):
        collection = self.get_collection()

        # Delete the task with the given task_id
        delete_res = collection.delete_one({"task_id": task_id})

        return delete_res.deleted_count > 0
