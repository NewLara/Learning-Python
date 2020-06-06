#get the age of the person
age = float(input('What is your age? '))

#Display value entered
print("You entered: ",format(age, '.1f'))

#Display age classification based on entered age
if age >= 20:
    print("You are an adult")
    
elif age >= 13 and age < 20:
    print ("You are a teenager")

elif age >= 1 and age < 13:
    print("You are a child")

else:
    print("You are an infant") 
        
