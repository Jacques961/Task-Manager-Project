from Task import Task
from user import user
import re
import datetime
import os
# adding the users code
usersInfo = []
def registerUser():
        path = r'C:\Users\jacqu\Desktop\intern\Week2\Day5\users.txt'
        print('You are creating an account.....')
        userName = input("Enter your username: ")
        while not userName:
            userName = input('User name is required: ')
            
        password = input("Enter your password (Must be 5 characters, with combination of letters, characters,symbols): ")
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$'
            
        while len(password) != 5 and not re.match(pattern, password):
            password = input('Must be 5 characters, with combination of letters, characters,symbols: ')
            
        newUser = user(userName,password)
        usersInfo.append(newUser)
        
        with open(path, 'a') as f:
            f.write('User ' + (str)(userName) + ' Password ' + (str)(password) + '\n')    
        return newUser

def users():
    path = r'C:\Users\jacqu\Desktop\intern\Week2\Day5\users.txt'
    if not os.path.exists(path):
        with open(path, 'w') as f:
            pass
    with open(path, 'r') as f:
        if not f.read(1):
            print('No users yet.\nYou have to register a user to use the app.')
            result = registerUser()
            return result
        else:
            userName = input('Log in.\nEnter you username: ')
            while not userName:
                userName = input('User name is required: ')
            
            with open(path, 'r') as f:
                for line in f:
                    if len(line)!= 0 and line.split()[1] == userName:
                        password = input('Enter your password: ')
                        if line.split()[3] == password:
                            print('Welcome ' + userName)
                            result = user(userName, password)
                            return result
                        else:
                            while password != line.split()[3]:
                                password = input('Incorrect password. Please try again: ')
                            print('Welcome ' + userName)
                            result = user(userName, password)
                            return result
                    
                print('User not found')
                result = registerUser()
                return result
                            
# Menu
def menu():
    return(
        '\nChoose from the following menu:\n'
        + '1. View the tasks.\n'
        + '2. Add a task.\n'
        + '3. Delete a task.\n'
        + '4. Update a task\n'
        + '5. Check if task is overdue\n'
        + '6. Mark task as completed\n'
        + '7. Sort task by status\n'
        + '8. Sort task by priority\n'
        + '9. Clear all tasks\n'
        + '10. Go back to log in\n'
        + '0. Quit\n'
    )
    

def main():
    while True:
        userName = users()
            
        userName.loadTasks()
        
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
                if userName.getList().getTasksNumber() == 0:
                    print('There are no tasks in the list.')
                else:
                    print(userName.__str__())
                        
            if choice == 2:
                # add task to the tasks file
                added = userName.getList().addTask()
                if added == True:
                    userName.saveTask()
                                
            if choice == 3:
                print('\nDeleting a task.')
                index = input('Enter the index of the task to delete: ')
                
                while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > userName.getList().getTasksNumber()):
                    index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
                sure = input('Enter you password to confirm deletion or 0 to cancel: ')
                userPass = userName.getPassword()
                
                while sure != '0':
                    if sure == userPass:
                        break
                    while sure != userPass:
                        if sure == '0':
                            print('\nDeletion cancelled')
                            break
                        sure = input('\nIncorrect password. Please enter your password: ')
                
                if sure == '0':
                    print('\nDeletion cancelled')
                    
                if sure == userPass:    
                    index = (int)(index)
                    deleted = userName.getList().removeTask(index)
                    if deleted:
                        userName.saveTasks()
                
                # deleting the task from the file
                # never modify a list while iterating over it
                # if deleted:
                #     with open('tasks.txt', 'r') as f:
                #         lines = f.readlines()
                #     start = (index - 1) * 7
                #     del lines[start:start+7]
                #     with open('tasks.txt', 'w') as f:
                #         f.writelines(lines)
                
            if choice == 4:
                print('\nUpdating a task.')
                index = input('Enter the index of the task to update: ')
                
                while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > userName.getList().getTasksNumber()):
                    index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                    
                
                index = (int)(index)
                updated = userName.getList().updateTask(index)
                
                if updated:
                    userName.saveTasks()
                        
            if choice == 5:
                index = input('Enter the index of the task to check: ')
                
                while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > userName.getList().getTasksNumber()):
                    index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                    
                index = (int)(index)
                overdue = userName.getList().checkIfOverdue(index)
                
                if overdue:
                    userName.saveTasks()
            
            if choice == 6:
                index = input('Enter the index of the task to mark: ')
                
                while not re.match(r"^[0-9]+$", index) or ((int)(index) < 0 or (int)(index) > userName.getList().getTasksNumber()):
                    index = input('\nInvalid index. Please enter an integer index in the range of indecies: ')
                
                index = (int)(index)
                marked  = userName.getList().markTaskDone(index)
                
                c = input("\nDo you want to delete task done? ('Y' for yes 'N' for no): ")
                while c.lower() not in ['y', 'n']:
                    c = input("\nInvalid choice. Choose 'Y' for yes 'N' for no: ")
                    
                if c in ['y', 'Y']:
                    deleted = userName.getList().removeTask(index)
                    if deleted:
                        userName.saveTasks()
                else:
                    if marked:
                        userName.saveTasks()
            
            if choice == 7:
                status = input("Enter 0 to sort the 'Completed', 1 to sort the 'Assigned', 2 to sort the 'Overdue': ")
                while not re.match(r"^[0-9]+$", status):
                    status = input("Choice must be 0 or 1 or 2: ")
                
                status = (int)(status)
                
                if status == 0:
                    userName.getList().sortByStatus('Completed.')
                elif status == 1:
                    userName.getList().sortByStatus('Assigned.')
                else:
                    userName.getList().sortByStatus('Overdue.')
            
            if choice == 8:
                status = input("Enter 0 to sort the 'Low', 1 to sort the 'Medium', 2 to sort the 'High': ")
                while not re.match(r"^[0-9]+$", status):
                    status = input("Choice must be 0 or 1 or 2: ")
                
                status = (int)(status)
                
                if status == 0:
                    userName.getList().sortByPriority('Low')
                elif status == 1:
                    userName.getList().sortByPriority('Medium')
                else:
                    userName.getList().sortByPriority('High')
            
            if choice == 9:
                sure = input('Enter you password to confirm deletion or 0 to cancel: ')
                userPass = userName.getPassword()
                
                while sure != '0':
                    if sure == userPass:
                        break
                    while sure != userPass:
                        if sure == '0':
                            print('\nDeletion cancelled')
                            break
                        sure = input('\nIncorrect password. Please enter your password: ')
                
                if sure == '0':
                    print('\nDeletion cancelled')
                    
                if sure == userPass:    
                    index = (int)(index)
                    userName.getList().clearTasks()
                    userName.clearTasksFromFile()
                        
            if choice == 10:
                break
            
            if choice == 0:
                print('\nGoodbye!\n')
                return
            
            

if __name__ == "__main__":
    main()