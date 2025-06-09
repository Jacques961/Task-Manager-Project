from Task import Task
import re

# intialize a list of Task
tasks = []

# Menu
def menu():
    return(
        'Choose from the following menu:\n'
        + '1. View the tasks.\n'
        + '2. Add a task.\n'
        + '3. Quit\n'
    )
    

def main():
    while True:
        print(menu())
        
        choice = input('User Choice: ')
        
        if not re.match(r"^[0-9]+$", choice):
            print('\nUser choice must be an integer.')
            continue
        
        choice = int(choice)
        
        if choice not in [1, 2, 3]:
            print('\nInvalid choice. Please choose a valid option.')
        
        if choice == 1:
            if not tasks:
                print('\nNo tasks available.\n')
            
            else:
                for t in tasks:
                    print(t.__str__())
                    
        if choice == 2:
            print('\nAdding a new task.')
            
            taskName = input('\nEnter task name: ')
            
            while len(taskName) == 0:
                if len(taskName) == 0:
                    print('Task name cannot be empty. Retype the task name: ')
                    
                    taskName = input('\nEnter task name: ')
            
            taskDescription = input('\nEnter task description: ')
            
            while len(taskDescription) == 0:
                if len(taskDescription) == 0:
                    print('Task description cannot be empty. Retype the task description: ')
                    
                    taskName = input('\nEnter task description: ')

            task = Task(taskName, taskDescription)
            
            tasks.append(task)
        
        if choice == 3:
            print('\nGoodbye!\n')
            break
            
            

if __name__ == "__main__":
    main()


