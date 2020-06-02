#Get teh percentage of males and percentage of females in a class
#get number of females and males
females = int(input('Enter the number of females in class : '))
males = int(input('Enter the number of males in class : '))

#set variables with calculations
totalStudents = (males + females)
malePercentage = males/totalStudents
femalePercentage = females/totalStudents

#display calculations on screen 
print('You entered',females, 'females and',males, 'males')
print('There are', format(malePercentage, '.0%'), 'males in the class')
print('There are', format(femalePercentage, '.0%'), 'females in the class')

