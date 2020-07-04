#program that prints instanciated  objects using the employee.py module with the Employee() class
import employee

def main():

    employee1 = employee.Employee("Susan Meyers", '47899' , 'Accounting', 'Vice President')
    employee2 = employee.Employee("Mark Jone", '39119' , 'IT', 'Programmer')
    employee3 = employee.Employee("Joy Rogers ", '81774' , 'Manufacturing', 'Engineer')

    print()
    print('-----------------------------------------------------------------------------------')
    print('{:<20}'.format('Name') + '{:<20}'.format('Id Number') + '{:<20}'.format('Department') +'{:<20}'.format('Title'))
    print('-----------------------------------------------------------------------------------')
    #print(employee1, '\n', employee2, '\n', employee3)
    print(employee1)
    print(employee2)
    print(employee3)
    


main() 
