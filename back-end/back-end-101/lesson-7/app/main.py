import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs='+', type=str,
                    help="Add task in file")
parser.add_argument("-l", "--list",
                    help="tasks in file", action='store_true')
parser.add_argument("-u", "--update", nargs='+',
                    help="Update task: ID and new description")
parser.add_argument("-d", "--delete", type=int,
                    help="Delete task from file by id")
args = parser.parse_args()

if args.add:
    description = ' '.join(args.add)    
    with open('file.txt', 'r') as file:
        lines_quantity = file.readlines()
        count = len(lines_quantity)

    with open('file.txt', 'a') as file:
        id = count + 1
        
        file.write(f"{id}: {description}" + '\n')

if args.list:
    with open('file.txt', 'r') as file:
        content = file.read()
    print(content)

if args.delete:
    try:
        with open('file.txt', 'r') as file: #read file
            lines = file.readlines()
        
        new_lines = [line for line in lines if line.strip() and int(line.split(':', 1)[0]) != args.delete] #filter lines
        
        if len(new_lines) == len(lines): #check if line deleted
            print("ID not found")
        else:
            renumbered_lines = [f"{i+1}: {line.split(':', 1)[1]}" for i, line in enumerate(new_lines)]
            with open('file.txt', 'w') as file: #rewrite file
                file.writelines(renumbered_lines)
    except FileNotFoundError:
        print("File not found")
    except (ValueError, IndexError):
        print("Error: incorrect line format in file")

if args.update:
    try:
        if len(args.update) < 2:
            print("Ошибка: укажите ID и описание")
        task_id = int(args.update[0])
        new_description = ' '.join(args.update[1:])
        with open('file.txt', 'r') as file:
            lines = file.readlines()
        found = False
        for i, line in enumerate(lines):
            if line.strip() and int(line.split(':', 1)[0]) == task_id:
                lines[i] = f"{task_id}: {new_description}\n"
                found = True
                break
        if not found:
            print(f"ID {task_id} not found")
        with open('file.txt', 'w') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("File not found")
    except (ValueError, IndexError):
        print("Error: incorrect line format in file")