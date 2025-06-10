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
    
    def addTask(self, task: Task):
        self.__todolist.append(task)
        print("Task added.")
    
    def removeTask(self, index: int):
        if index < 0 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            del self.__todolist[index-1]
            print("Task deleted.")
    
    def markTaskDone(self, index: int):
        if index < 0 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            self.__todolist[index-1].setStatus('C')
            print("Task marked as done.")
            
    def checkIfOverdue(self, index: int):
        if index < 0 or index > len(self.__todolist):
            raise IndexError("Index out of range.")
        else:
            task = self.__todolist[index-1]
            if task.getDuedate() < datetime.datetime.today() and task.getStatus() == 'Task Assigned.':
                print("Task is overdue.")
            else:
                print("Task is not overdue.")
    
    def updateTask(self, index: int):
        if index < 0 or index > len(self.__todolist):
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
            while taskpriority not in ['L', 'M', 'H']:
                taskpriority = input('\nInvalid priority. Please enter L for Low, M for Medium, or H for High: ')
            task.setPriority(taskpriority)
            
            taskcategory = input('\nEnter task category (Work, Personal, Shopping, Other): ')
            while taskcategory.lower() not in ['work', 'personal', 'shopping', 'other']:
                taskcategory = input('\nInvalid category. Please enter Work, Personal, Shopping, or Other: ')
            task.setCategory(taskcategory)
            
            
            print('Task updated.')
        
    def __str__(self):
        i = 1
        for task in self.__todolist:
            print('Task ' + (str)(i) + ': ' + task.__str__())
            i += 1