
#employee class that holds name and number attributes
class Employee2:
    def __init__(self, name, number):
        self.__name = name 
        self.__number = number 

    def setName (self, name):
        self.__name = name 

    def setNumber (self, number):
        self.__number = number 

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

#productionWorker class holds Shift (1 or 2 ) and hourly pay rate 
#workday is divided into two shifts, day and night 
#shiftNum holds 1 for day and 2 for night 
class ProductionWorker(Employee2):
    def __init__(self, name, number, shiftNum, payRate):
        Employee2.__init__(self, name, number)
        self.__shiftNum = shiftNum 
        self.__payRate = payRate

    def setShift(self,shiftNum):
        if shiftNum == '1':
            self.__shiftNum = "Day"
        else:
            self.__shiftNum = "Night"

    def getShift(self):        
        return self.__shiftNum

    def getPayRate(self):
        return self.__payRate

    