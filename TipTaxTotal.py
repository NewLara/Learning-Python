#Get the total of a food purchase with tip and tax, listing the tip and tax amounts seperately 
#User input of food amount 
foodAmount = float(input("Enter the total cost of your food : "))
#calculate tip
totalTip = foodAmount * .18
totalWithTip = totalTip + foodAmount

#calculate 7% tax
totalTax = foodAmount * .07
totalWithTax = foodAmount + totalTax

#total with tax and tip
finalTotal = totalWithTax + totalTip

#Display totals
print("You Entered $", format(foodAmount, ',.2f'))
print("Your 18% tip is: $", format(totalTip, ',.2f'))
print("Your 7% tax is: $", format(totalTax, ',.2f'))
print("Your total with tax and tip is: $", format(finalTotal, ',.2f'))


