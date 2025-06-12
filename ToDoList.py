from Task import Task
import datetime

class ToDoList():
    def __init__(self, toDo: list = None):
        self.setToDoList(toDo)
        
    def setToDoList(self, toDo: list):
        if toDo is None:
            self.__todolist = []
        
        else:
            for task in toDo:
                if isinstance(task, Task):
                    self.__todolist.append(task)
                else:
                    raise TypeError("Invalid task type. Only Task objects are allowed.")
                
    def getTasksNumber(self):
        return (len)(self.__todolist)
    
    def addTaskFromFile(self, task: Task):
        self.__todolist.append(task)
        
    def addTask(self):
        print('\nAdding a new task.')
    
        taskName = input('\nEnter task name or 0 to go back: ')

        if taskName == '0':
            return
        
        while len(taskName) == 0:
            if taskName == '0':
                break
            if len(taskName) == 0:
                taskName = input('Task name cannot be empty. Retype the task name or 0 to go back: ')

        if taskName == '0':
            return

        taskDescription = input('\nEnter task description or 0 to go back: ')

        if taskDescription == '0':
            return
        
        while len(taskDescription) == 0:
            if taskDescription == '0':
                break
            if len(taskDescription) == 0:
                taskName = input('Task description cannot be empty. Retype the task description or 0 to go back: ')

        if taskDescription == '0':
            return

        taskduedate = input('\nEnter task due date (date format YYYY-MM-DD) or 0 to go back: ')

        if taskduedate == '0':
            return 
        
        while True:
            if taskduedate == '0':
                break
            try:
                taskduedate = datetime.datetime.strptime(taskduedate, "%Y-%m-%d")
                break
            except ValueError:
                taskduedate = input("\nInvalid date format. Please enter the date in YYYY-MM-DD format or 0 to go back: ")

        if taskduedate == '0':
            return
        
        taskpriority = input('\nEnter task priority (L for Low, M for Medium, H for High) or 0 to go back: ')

        if taskpriority == '0':
            return
        
        taskpriority = taskpriority.upper() 
        while taskpriority not in ['L', 'M', 'H']:
            if taskpriority == '0':
                break
            taskpriority = input('\nInvalid priority. Please enter L for Low, M for Medium, or H for High or 0 to go back: ')

        taskcategory = input('\nEnter task category (Work, Personal, Shopping, Other) or 0 to go back: ')

        if taskcategory == '0':
            return
        
        taskcategory = taskcategory.lower()
        while taskcategory not in ['work', 'personal', 'shopping', 'other']:
            if taskcategory == '0':
                break
            taskcategory = input('\nInvalid category. Please enter Work, Personal, Shopping, or Other or 0 to go back: ')

        task = Task(len(self.__todolist),taskName,taskDescription,taskduedate,taskpriority,taskcategory)
        self.__todolist.append(task)
        print("Task added.")
        return True
    
    def removeTask(self, index: int):
        if index < 1 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            del self.__todolist[index-1]
            for i in range(index-1, len(self.__todolist)):
                self.__todolist[i].setId(i+1)
            print("Task deleted.")
            return True
    
    def markTaskDone(self, index: int):
        if index < 1 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            self.__todolist[index-1].setStatus('C')
            print("Task marked as done.")
            return True
            
    def checkIfOverdue(self, index: int):
        if index < 1 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            task = self.__todolist[index-1]
            if task.getDuedate() < datetime.datetime.today() and task.getStatus() == 'Assigned.':
                print("Task is overdue.")
                task.setStatus('OD')
                return True
            else:
                print("Task is not overdue.")
    
    def updateTask(self, index: int):
        if index < 1 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            task = self.__todolist[index-1]
            
            title = input('Enter new title (Keep blank if no update): ')
            if title:
                task.setTitle(title)
            
            description = input('Enter new description (Kepp blank if no update): ')
            if description:
                task.setDescription(description)
            
            duedate = input("Enter new due date (YYYY-MM-DD) or leave blank to keep current: ")
            if duedate:
                while True:
                    try:
                        duedate = datetime.datetime.strptime(duedate, "%Y-%m-%d")
                        task.setDuedate(duedate)
                        break
                    except ValueError:
                        duedate = input("\nInvalid date format. Please enter the date in YYYY-MM-DD format: ")
            
            taskpriority = input('\nEnter new task priority (L for Low, M for Medium, H for High): ')
            
            taskpriority = taskpriority.title()
            while taskpriority not in ['L', 'M', 'H']:
                taskpriority = input('\nInvalid priority. Please enter L for Low, M for Medium, or H for High: ')
            task.setPriority(taskpriority)
            
            taskcategory = input('\nEnter task category (Work, Personal, Shopping, Other): ')
            
            taskcategory = taskcategory.lower()
            while taskcategory.lower() not in ['work', 'personal', 'shopping', 'other']:
                taskcategory = input('\nInvalid category. Please enter Work, Personal, Shopping, or Other: ')
            task.setCategory(taskcategory)
            
            
            print('Task updated.')
            return True
    
    def strWithIndex(self, index: int):
        if index < 1 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            task = self.__todolist[index-1]
            return('Task ' + (str)(index) + ': ' + task.__str__() + '\n')
            
    def __str__(self):
        out = ''
        for i, task in enumerate(self.__todolist, 1):
            out += ('\nTask ' + (str)(i) + ': ' + task.__str__() + '\n')
        return out
    