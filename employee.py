#class to initialize, set and get employee attributes 

class Employee :
    #constructor for class 
    def __init__(self,name, idNum, dept, title):
        self.name = name
        self.idNum = idNum
        self.dept = dept
        self.title = title

#getters and setters for class 
    def set_name(self, name):
         self.name = name
    def set_idNum(self, idNum):
        self.idNum= idNum
    def set_dept(self, dept):
        self.dept= dept
    def set_title(self, title):
        self.title = title
    def get_name(self):
        return self.name
    def get_idNum(self):
        return self.idNum
    def get_dept(self):
        return self.dept
    def get_title(self):
        return self.title
    #return the state of the object
    def __str__(self):        
        return '{:<20}'.format(self.name) + '{:<20}'.format(self.idNum) + '{:<20}'.format(self.dept) + '{:<20}'.format(self.title)
            
                 
        

