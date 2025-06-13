import datetime 
class Task():
    def __init__(self, id: int, title: str = None, description: str = None, duedate: datetime = datetime.datetime.today(), priority: str = None, category: str = None, status: str = 'A'):
        self.setTask(id,title, description, duedate, priority, category)
        self.__status = status # not set by the user when first adding the task
    
    def setTask(self,id: int, title: str, description: str, duedate: datetime, priority: str, category: str):
        self.setId(id)
        self.setTitle(title)
        self.setDescription(description)
        self.setDuedate(duedate)
        self.setPriority(priority)
        self.setCategory(category)
        
    def setId(self, id: int):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def setTitle(self, title: str):
        if not title is None:
            self.__title = title
        else:
            self.__title = None
    
    
    def setDescription(self, description: str):
        if not description is None:
            self.__description = description
        else:
            self.__description = None
    
    def setStatus(self, status: str):
        if status in ['A' , 'C', 'OD']:
            self.__status = status
            
        else:
            self.__status = 'A'
    
    def setDuedate(self, duedate: datetime):
        if not duedate is None:
            if duedate < datetime.date.today():
                self.__duedate = datetime.datetime.today()
            else:
                self.__duedate = datetime.datetime.today()
    
    def setPriority(self, priority: str):
        if priority in ['L', 'M', 'H']:
            self.__priority = priority
        else:
            self.__priority = 'M'
    
    def setCategory(self, category: str):
        if category in ['work', 'personal', 'shopping', 'other']:
            self.__category = category
        else:
            self.__category = 'Other'
            
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getStatus(self):
        if self.__status == 'A':
            return 'Assigned.'
        if self.__status == 'C':
            return 'Completed.'
        if self.__status == 'OD':
            return 'Overdue.'
        
    def getDuedate(self):
        return self.__duedate
    
    def getPriority(self):
        if self.__priority == 'L':
            return "Low"
        if self.__priority == 'M':
            return 'Medium'
        if self.__priority == 'H':
            return 'High'
        
    def getCategory(self):
        return self.__category
    
    def __str__(self):
        return self.__repr__()
       
    
    def __repr__(self):
         return ((str)(self.getTitle()) + '\nDescription: ' + (str)(self.getDescription()) 
                 + '\nDueDate: ' + (str)(self.getDuedate()) + '\nPriority: ' + self.getPriority() + '\nCategory: ' + self.getCategory() + '\nStatus: ' + (str)(self.getStatus()))