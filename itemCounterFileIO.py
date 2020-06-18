#Lara Caves
#6/13/20
#names.txt exists already in same directory for reading and editing
#user can create new file to add names, then see contents of file
#This program gets a file name from user, determines user action path, implements action,
#reads, prints names in file and the number of names in the file, closes teh file

def main():     
     
    try:
        #get file name from user       
        fileName = input('Enter the name of the file: ')
        
        #get action from user
        action = input('Would you like to Add (A), Edit (E), or Read (R) the file?')        
        if action == 'A':
            addFile(fileName)           
        elif action == 'E':
            editFile(fileName)        
        else:
            readFile(fileName)
    except Exception as err:
        print(err)
        
#**********************************
#*********FUNCTIONS****************
#**********************************
#ADD
def addFile(fileName):
    print()
    print('********************************')
    print("You chose to ADD '{}' ".format(fileName))
    print('If the file exists, existing data will be overwritten'.format(fileName))
    print('********************************')
    print()
    
    #create new file or open if exists
    names_file = open(fileName, mode = 'w')
    print()
    print("Adding the file '{}' .....".format(fileName))

    #write user provided names to file 
    nameAdded = input("Please enter a first name to add to the file, or enter 'Q' to quit: ")
    while nameAdded != 'Q':
        names_file.write(nameAdded +'\n')
        nameAdded = input("Please enter a name to add to the file, or enter 'Q' to quit: ")
    print()
    print('You chose to quit adding names.')
    print('Closing file and preparing to read contents.....')
    names_file.close()
    
    #Call readFile function
    readFile(fileName)
    
#EDIT
def editFile(fileName):
    #edit file
    print()
    print('********************************')
    print("You chose to EDIT '{}' ".format(fileName))
    print('If the file exists, data will be added to end of the file'.format(fileName))
    print('********************************')
    print()
    
    names_file = open(fileName, mode = 'a')
    print()   
    print("Opening the file '{}' .....".format(fileName))
    print()

    #write user provided names to file 
    nameAdded = input("Please enter a name to add to the file, or enter 'Q' to quit: ")
    while nameAdded != 'Q':
        names_file.write(nameAdded +'\n')
        nameAdded = input("Please enter a name to add to the file, or enter 'Q' to quit: ")
    print()
    print('You chose to quit adding names.')
    print('Closing file and preparing to read contents.....')
    names_file.close()
    
    #Call readFile function
    readFile(fileName)

#READ
def readFile(fileName):
    #open file for READ
    names_file = open(fileName, mode = 'r')
    print()
    #read file 
    print('...')
    print("Reading file '{}' .....".format(fileName))
    print()
    print("The names in the file '{}' are ....".format(fileName))
    
    #iterate through names in file, accumulating count, and printing names
    count = 0
    for name in names_file:
        name = name.rstrip('\n')
        count += 1
        print(name)
    print()

    #print the name count in file 
    print("There are {} names in the file '{}'. ".format(count, fileName))          
    print()
    
    #close file
    print('Closing file.......')
    names_file.close()
    print('Goodbye.')

#call main function
main()
