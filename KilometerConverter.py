#Lara Caves
#6/13/20
#get user input in kilometers and convert to miles
#utilize a myModule method, and in program functions
#for conversions and printing results
import myModule

def main():
    try:
        #get distance in kilometers
        kilo = float(input("Enter distance in kilometers: "))
        print()
        
        #convert by calling method in myModule
        print('I can convert to miles by calling a MODULE METHOD....')
        print('Then I call an IN PROGRAM FUNCTION to print the results')
        miles = myModule.convertToMiles(kilo)
        print()
        # call print conversion
        printConv(kilo, miles)    
        
        #call an in program function to convert
        print()
        print('OR I can convert to miles by calling an IN PROGRAM FUNCTION ....')
        print('This function calls the print funtion to print the results')
        print()
        convert(kilo)
        

       
    except Exception as err:
        print(err)
        
    
def convert(x):
    miles =  x * 0.6214
    printConv(x, miles)


def printConv(x, miles):
    print("........{} kilometers is equal to {} miles. ".format(format(x, '.2f'), format(miles, '.2f')))

main()
    

