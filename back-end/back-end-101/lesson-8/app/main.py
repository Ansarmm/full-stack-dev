import argparse
import json
import os

json_path = "../data/data.json"
txt_path = "file.txt"

def add_task():
    description = ' '.join(args.add)
    if not description.strip():
        print("Error: task description is empty")
        return

    # Get ID
    if os.path.exists(txt_path):
        with open(txt_path, 'r') as file:
            lines_quantity = file.readlines()
            count = len(lines_quantity)
    else:
        count = 0

    task_id = count + 1

    # Write in .txt
    with open(txt_path, 'a') as file:
        file.write(f"{task_id}: {description}\n")

    # Write in JSON file
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({"id": task_id, "description": description})

    with open(json_path, 'a') as file:
        json.dump(data, file, indent=4)

    print(f"Task #{task_id} added.")
    

def list_tasks():
    try:
        with open(json_path, 'r') as file:
            content = json.load(file)
            if not content:
                print("No tasks found.")
            else:
                for task in content:
                    print(f"{task['id']}: {task['description']}")
    except FileNotFoundError:
        print("Error: data.json file not found.")
    except json.JSONDecodeError:
        print("Error: data.json is empty or corrupted.")

def delete_task():
    try:
        task_id = args.delete

        # Delete in file.txt
        with open(txt_path, 'r') as file:
            lines = file.readlines()

        new_lines = [line for line in lines if line.strip() and int(line.split(':', 1)[0]) != task_id]

        if len(new_lines) == len(lines):
            print(f"Task with ID {task_id} not found.")
            return

        renumbered_lines = [f"{i+1}: {line.split(':', 1)[1]}" for i, line in enumerate(new_lines)]
        with open(txt_path, 'w') as file:
            file.writelines(renumbered_lines)

        # Delete in JSON
        with open(json_path, 'r') as file:
            data = json.load(file)

        new_data = [task for task in data if task["id"] != task_id]
        for i, task in enumerate(new_data, start=1):
            task["id"] = i

        with open(json_path, 'w') as file:
            json.dump(new_data, file, indent=4)

        print(f"Task #{task_id} deleted.")
    
    except FileNotFoundError:
        print("Error: file.txt or data.json not found.")
    except (ValueError, IndexError):
        print("Error: incorrect file format.")
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")

def update_task():
    try:
        if len(args.update) < 2:
            print("Error: specify ID and new description.")
            return

        task_id = int(args.update[0])
        new_description = ' '.join(args.update[1:])

        # Update file.txt
        with open(txt_path, 'r') as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            if line.strip() and int(line.split(':', 1)[0]) == task_id:
                lines[i] = f"{task_id}: {new_description}\n"
                found = True
                break

        if not found:
            print(f"Error: Task #{task_id} not found in file.txt.")
        else:
            with open(txt_path, 'w') as file:
                file.writelines(lines)

        # Update JSON
        with open(json_path, 'r') as file:
            data = json.load(file)

        found = False
        for task in data:
            if task["id"] == task_id:
                task["description"] = new_description
                found = True
                break

        if not found:
            print(f"Error: Task #{task_id} not found in JSON.")
        else:
            with open(json_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Task #{task_id} updated.")

    except FileNotFoundError:
        print("Error: file.txt or data.json not found.")
    except (ValueError, IndexError):
        print("Error: invalid ID or file format.")
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")

# Arg parse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs='+', type=str, help="Add task")
parser.add_argument("-l", "--list", action='store_true', help="List tasks")
parser.add_argument("-u", "--update", nargs='+', help="Update task: ID and new description")
parser.add_argument("-d", "--delete", type=int, help="Delete task by ID")
args = parser.parse_args()

if args.add:
    add_task()
if args.list:
    list_tasks()
if args.delete:
    delete_task()
if args.update:
    update_task()
