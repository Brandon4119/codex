import requests

URL = "http://127.0.0.1:5000/tasks"

def update_task(summary, description):
    update_task_data = {
        "summary": summary,
        "description": description
    }
    url = "%s/%s" % (URL, task_id)
    response = requests.put(url, json=update_task_data) #put delete
    if response.status_code == 204:
        print("Task updated successfully.")
    else:
        print("Task update failed.")



if __name__ == "__main__":
    print("Update task: ")
    id = input("id: ")
    summary = input("Summary: ")
    description = input("Description: ")
    update_task(summary, description, id)