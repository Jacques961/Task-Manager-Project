from ToDoList import ToDoList
import os
from itertools import islice
import datetime
from Task import Task

class user():
    def __init__(self, name: str = None, password: str = None):
        self.setUser(name,password)
        self.__list = ToDoList()
        
    def getList(self):
        return self.__list
    
    def setUser(self, name: str, password: str):
        self.setName(name)
        self.setPassword(password)
        
    def setName(self, name: str):
        if name == None:
            self.__name = None
        else:
            self.__name = name
    
    def setPassword(self, password: str):
        if password == None:
            self.__password = None
        else:
            self.__password = password
    
    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password
    
    def loadTasks(self):
        path = r'C:\Users\jacqu\Desktop\intern\Week2\Day5'
        path = os.path.join(path, self.getName() + '.txt')
        if not os.path.exists(path):
            with open(path, 'w') as f:
                print('New empty tasks file created for ' + (str)(self.getName()) + '.')
                pass
        else:
            with open(path, 'r') as f:
                if not f.read(1):
                    print('You already have a tasks file, but empty.')
                else:
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
                        
                        task = Task(lines[0].split(': ')[0].split()[1],taskName,taskDescripiton,taskDuedate,taskPriority,taskCategory,taskStatus)
                        self.__list.addTaskFromFile(task)
                        
    def saveTasks(self):
        with open(os.path.join(r'C:\Users\jacqu\Desktop\intern\Week2\Day5', self.getName() + '.txt'), 'w') as f:
            f.write(self.__list.__str__())
    
    def saveTask(self):
        with open(os.path.join(r'C:\Users\jacqu\Desktop\intern\Week2\Day5', self.getName() + '.txt'), 'a') as f:
            f.write('\n' + self.__list.strWithIndex(self.__list.getTasksNumber()))
            
    def clearTasksFromFile(self):
         with open(os.path.join(r'C:\Users\jacqu\Desktop\intern\Week2\Day5', self.getName() + '.txt'), 'w') as f:
             print("Tasks file cleared.")
             pass
            
    def __str__(self):
        return ('User: ' + (str)(self.getName())
                + '\nHas the following tasks:\n' + '_______________________________\n'
                + self.__list.__str__())
