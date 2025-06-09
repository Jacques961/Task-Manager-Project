class Task():
    def __init__(self, title: str = None, description: str = None):
        self.setTask(title, description)
        self.__status = 'A' # not set by the user when first adding the task
    
    def setTask(self, title: str, description: str):
        self.setTitle(title)
        self.setDescription(description)
        
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
    
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getStatus(self):
        if self.__status == 'A':
            return 'Task Assigned.'
        if self.__status == 'C':
            return 'Task Completed.'
        if self.__status == 'OD':
            return 'Task Overdue.'
    
    def __str__(self):
        return self.__repr__()
       
    
    def __repr__(self):
         return ('\nTask: ' + (str)(self.getTitle()) + '\nDescription: ' + (str)(self.getDescription()) + '\nStatus: ' + (str)(self.getStatus()))