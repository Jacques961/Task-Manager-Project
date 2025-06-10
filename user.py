from ToDoList import ToDoList

class user():
    def __init__(self, name: str = None, email: str = None, password: str = None):
        self.setUser(name,email,password)
        self.list = ToDoList()
    
    def setUser(self, name: str, email: str, password: str):
        self.setName(name)
        self.setEmail(email)
        self.setPassword(password)
        
    def setName(self, name: str):
        if name == None:
            self.__name = None
        else:
            self.__name = name
    
    def setEmail(self, email: str):
        if email == None:
            self.__email = None
        else:
            self.__email = email
    
    def setPassword(self, password: str):
        if password == None:
            self.__password = None
        else:
            self.__passsword = password
    
    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def __str__(self):
        return ('User: ' + (str)(self.getName()) + '\nEmail: ' + (str)(self.getEmail())
                + '\nHas the following tasks:\n' + '_______________________________\n'
                + self.list.__str__())