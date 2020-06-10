   #open text file (default mode='r'...meaning read)
#myFile = open("test.txt")

   #read and print file contents
#print(myFile.read())

   #set cursor back to index[0]
#myFile.seek(0)

   #read and print file contents
#print(myFile.read())

   #use readline to set cursor back to index[0]
##print(myFile.readline())
##print(myFile.readline())
##print(myFile.readline())

   #use readlineS to read all of file with esc char's
#print(myFile.readlines())

   #manually close file
#myFile.close()

#---------------------------------------------------------

   #use 'with as' to prevent needing to use .close()
##with open('test.txt') as myFile:
##    print(myFile.readlines())

   #read and write to file using mode='r+' will overwrite #of char that is already in file 
##with open('test.txt', mode='r+') as myFile:
##    text = myFile.write('hey it is me!')
##    print(text)

     #append to EOF using mode='a'  
##with open('test.txt', mode='a') as myFile:
##    text = myFile.write(':)')
##    print(text)

    #write to file using mode='w'  will overwrite all of file
    #will also create a file if it does not already exist 
with open('test.txt', mode='w') as myFile:
    text = myFile.write(':)')
    print(text)




