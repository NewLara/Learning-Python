#get the age of the person

age = float(input("Enter your age: "))

if age >=1:
    print("You entered: ",format(age, '.0f'))
else:
    print("You entered: ",format(age, '.1f'))

if age >= 20:
    print("You are an adult")
    
elif age >= 13 and age < 20:
    print ("You are a teenager")

elif age >= 1 and age < 13:
    print("You are a child")

else:
    print("You are an infant") 
        
