from Task import Task
from ToDoList import ToDoList
import re
import datetime
import os
from itertools import islice

# intialize a list of Task
path = r'C:\Users\jacqu\Desktop\intern\Week2\Day3\tasks.txt'
tasks = ToDoList()
if not os.path.exists(path):
    with open('tasks.txt', 'w') as f:
	    pass
 
else:
    with open(path, 'r') as f:
        while True:
            lines = list(islice(f, 7))
            if not lines:
                break
            taskName = lines[0].split(': ')[1].strip()
            taskDescripiton = lines[1].split(': ')[1].strip()
            date = lines[2].split(': ')[1].strip()
            taskDuedate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            taskPriority = lines[3].split(': ')[1][0].strip()
            taskCategory = lines[4].split(': ')[1].strip()
            if lines[5].split(': ')[1][0] == 'O':
                taskStatus = 'OD'
            else:
                taskStatus = lines[5].split(': ')[1][0].strip()
            
            task = Task(taskName,taskDescripiton,taskDuedate,taskPriority,taskCategory,taskStatus)
            tasks.addTask(task)

# Menu
def menu():
    return(
        '\nChoose from the following menu:\n'
        + '1. Create a to do list\n'
        + '2. View the tasks.\n'
        + '3. Add a task.\n'
        + '4. Delete a task.\n'
        + '5. Update a task\n'
        + '6. Check if task is overdue\n'
        + '7. Mark task as completed\n'
        + '0. Quit\n'
    )
    

def main():
    global tasks
    while True:
        print(menu())
        
        choice = input('User Choice: ')
        
        if not re.match(r"^[0-9]+$", choice):
            print('\nUser choice must be an integer.')
            continue
        
        choice = int(choice)
        
        if choice not in [0, 1, 2, 3, 4, 5, 6, 7]:
            print('\nInvalid choice. Please choose a valid option.')
        
        if choice == 1:
            tasks = ToDoList()
            print('You have created a to do list with no tasks in it.')
            
        if choice == 2:
            if not tasks:
                print('There are no tasks in the list.')
            else:
                print(tasks.__str__())
                    
        if choice == 3:
            print('\nAdding a new task.')
            
            task = Task()
            taskName = input('\nEnter task name or 0 to go back: ')
            
            if taskName == '0':
                continue
            
            while len(taskName) == 0:
                if taskName == '0':
                    break
                if len(taskName) == 0:
                    taskName = input('Task name cannot be empty. Retype the task name or 0 to go back: ')
                    
            if taskName == '0':
                continue
                    
            task.setTitle(taskName)
            
            taskDescription = input('\nEnter task description or 0 to go back: ')
            
            if taskDescription == '0':
                continue
            
            while len(taskDescription) == 0:
                if taskDescription == '0':
                    break
                if len(taskDescription) == 0:
                     taskName = input('Task description cannot be empty. Retype the task description or 0 to go back: ')
            
            if taskDescription == '0':
                continue
            
            task.setDescription(taskDescription)
            
            taskduedate = input('\nEnter task due date (date format YYYY-MM-DD) or 0 to go back: ')
            
            if taskduedate == 0:
                continue 
            
            while True:
                if taskduedate == 0:
                    break
                try:
                    duedate = datetime.datetime.strptime(taskduedate, "%Y-%m-%d")
                    task.setDuedate(duedate)
                    break
                except ValueError:
                    taskduedate = input("\nInvalid date format. Please enter the date in YYYY-MM-DD format or 0 to go back: ")
            
            if taskduedate == 0:
                continue
            
            taskpriority = input('\nEnter task priority (L for Low, M for Medium, H for High) or 0 to go back: ')
            
            if taskpriority == '0':
                continue
            
            while taskpriority not in ['L', 'M', 'H']:
                if taskpriority == '0':
                    break
                taskpriority = input('\nInvalid priority. Please enter L for Low, M for Medium, or H for High or 0 to go back: ')
            task.setPriority(taskpriority)
            
            taskcategory = input('\nEnter task category (Work, Personal, Shopping, Other) or 0 to go back: ')
            
            if taskcategory == '0':
                continue
            
            while taskcategory.lower() not in ['work', 'personal', 'shopping', 'other']:
                if taskcategory == '0':
                    break
                taskcategory = input('\nInvalid category. Please enter Work, Personal, Shopping, or Other or 0 to go back: ')
            task.setCategory(taskcategory)
            
            added  = tasks.addTask(task)
            
            # add task to the tasks file
            if added == True:
                with open('tasks.txt', 'a') as f:
                    f.write(tasks.strWithIndex(tasks.getTasksNumber()))
        
        if choice == 4:
            print('\nDeleting a task.')
            index = input('Enter the index of the task to delete: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            index = (int)(index)
            deleted = tasks.removeTask(index)
            
            # deleting the task from the file
            # never modify a list while iterating over it
            # if deleted:
            #     with open('tasks.txt', 'r') as f:
            #         lines = f.readlines()
            #     start = (index - 1) * 7
            #     del lines[start:start+7]
            #     with open('tasks.txt', 'w') as f:
            #         f.writelines(lines)
            
            if deleted:
                with open('tasks.txt', 'w') as f:
                    f.write(tasks.__str__())
        
        if choice == 5:
            print('\nUpdating a task.')
            index = input('Enter the index of the task to update: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            
            index = (int)(index)
            updated = tasks.updateTask(index)
            
            if updated:
                with open('tasks.txt', 'w') as f:
                    f.write(tasks.__str__())
                    
        if choice == 6:
            index = input('Enter the index of the task to check: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            index = (int)(index)
            overdue = tasks.checkIfOverdue(index)
            
            if overdue:
                with open('tasks.txt', 'w') as f:
                    f.write(tasks.__str__())
        
        if choice == 7:
            index = input('Enter the index of the task to mark: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
            
            index = (int)(index)
            marked  = tasks.markTaskDone(index)
            
            c = input("\nDo you want to delete task done? ('Y' for yes 'N' for no): ")
            while c.lower() not in ['y', 'n']:
                c = input("\nInvalid choice. Choose 'Y' for yes 'N' for no: ")
                
            if c in ['y', 'Y']:
                deleted = tasks.removeTask(index)
                if deleted:
                    with open('tasks.txt', 'w') as f:
                        f.write(tasks.__str__())
            else:
                if marked:
                    with open('tasks.txt', 'w') as f:
                        f.write(tasks.__str__())
            
        if choice == 0:
            print('\nGoodbye!\n')
            break
            
            

if __name__ == "__main__":
    main()


