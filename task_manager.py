from Task import Task
from ToDoList import ToDoList
import re
import datetime

# intialize a list of Task
tasks = ToDoList()

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
                tasks.__str__()
                    
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
            
            tasks.addTask(task)
        
        if choice == 4:
            print('\nDeleting a task.')
            index = input('Enter the index of the task to delete: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            
            index = (int)(index)
            tasks.removeTask(index)
        
        if choice == 5:
            print('\nUpdating a task.')
            index = input('Enter the index of the task to update: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            
            index = (int)(index)
            tasks.updateTask(index)
        
        if choice == 6:
            index = input('Enter the index of the task to check: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
            index = (int)(index)
            tasks.checkIfOverdue(index)
        
        if choice == 7:
            index = input('Enter the index of the task to mark: ')
            
            while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > tasks.getTasksNumber()):
                index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
            
            index = (int)(index)
            tasks.markTaskDone(index)
            
            c = input("\nDo you want to delete task done? ('Y' for yes 'N' for no): ")
            while c.lower() not in ['y', 'n']:
                c = input("\nInvalid choice. Choose 'Y' for yes 'N' for no: ")
                
            if c in ['y', 'Y']:
                tasks.removeTask(index)
            
            
        if choice == 0:
            print('\nGoodbye!\n')
            break
            
            

if __name__ == "__main__":
    main()


