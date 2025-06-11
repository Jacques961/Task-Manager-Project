import os
from itertools import islice
from Task import Task
from ToDoList import ToDoList

path = r'C:\Users\jacqu\Desktop\intern\Week2\Day3\tasks.txt'

todo = ToDoList()
if not os.path.exists(path):
    with open('tasks.txt', 'w') as f:
	    pass
 
else:
    with open(path, 'r') as f:
        while True:
            lines = list(islice(f, 7))
            if not lines:
                break
            taskName = lines[0].split(': ')[1]
            taskDescripiton = lines[1].split(': ')[1]
            taskDuedate = lines[2].split(': ')[1]
            taskPriority = lines[3].split(': ')[1]
            taskCategory = lines[4].split(': ')[1]
            taskStatus = lines[5].split(': ')[1]
            
            task = Task(taskName,taskDescripiton,taskDuedate,taskPriority,taskCategory,taskStatus)
            todo.addTask(task)

            # print(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5])
            print(taskName)
            