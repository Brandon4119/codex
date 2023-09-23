import requests

URL = "http://127.0.0.1:5000/tasks"

def delete_task(summary, description):
    task_data = {
        "summary": summary,
        "description": description
    }
    response = requests.delete(URL, json=task_data) #put delete
    if response.status_code == 204:
        print("Task delete successfully.")
    else:
        print("Task Delete failed.")



if __name__ == "__main__":
    print("Delete task: ")
    summary = input("Summary: ")
    description = input("Description: ")
    delete_task(summary, description)