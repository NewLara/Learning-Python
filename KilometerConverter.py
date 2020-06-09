import myModule


#get distance in kilometers
kilo = float(input("Enter distance in kilometers: "))

#call method from the module to convert
miles = myModule.convertToMiles(kilo)

#print conversion
print("{} kilometers is equal to {} miles. ".format(format(kilo, '.2f'), format(miles, '.2f')))

