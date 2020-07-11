import employee2

def main():
    #program main creates object of employee2.ProductionWorker and prompts user 
    # to enter data for each class attribute
    #store data in object then use getters() to retrieve and display   

    name = input("Enter the employee name: ")
    empNum = int(input("Enter employee number: "))
    shiftNum = input("Enter the employee shift number 1 for 'Day, 2 for 'Night':  ")   
    payRate = float(input("Enter hourly rate: "))

    worker1 = employee2.ProductionWorker(name, empNum, shiftNum, payRate)

    print()
    print('--------------------------------------------------------------------------')
    print('{:<20}'.format('Name') + '{:<20}'.format('Employee Number') +
     '{:<20}'.format('Shift') +'{:<20}'.format('Pay Rate'))
    print('--------------------------------------------------------------------------')    
    print('{:<20}'.format(worker1.getName()) + '{:<20}'.format(worker1.getNumber()) + 
    '{:<20}'.format(worker1.getShift()) + '{:<20}'.format(worker1.getPayRate()))

   
main()