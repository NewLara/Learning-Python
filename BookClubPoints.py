#get the number of books bought in a month

numOfBooks = int(input("How many books have you purchased this month: "))

#display number of points earned
if numOfBooks >= 8:
    print("You have earned 60 points!")
elif numOfBooks >= 6 and numOfBooks < 8:
    print ("You have earned 30 points")
elif numOfBooks >= 4 and numOfBooks < 6:
    print ("You have earned 15 points")
elif numOfBooks >= 2 and numOfBooks < 4:
    print ("You have earned 5 points")
else:
    print("You have earned 0 points")
    
