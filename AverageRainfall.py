#get number of years
numOfYears = int(input("How many years?: "))
numOfMonths = numOfYears*12
totalInches = 0.0

#loop number of years entered to add rain amounts to accumulator                 
for year in range(numOfYears):    #iterate once for each year
    print()
    print('Year', year+1)
    print('------------')
    for month in range(12):        #iterate 12x's for each year
        totalMonth = float(input('How many inches in month {}:  '.format(month+1)))
        totalInches += totalMonth
        avgRainfall = totalInches/numOfMonths
#Table Header
print()
print('-------------------------------')
print('Total\tTotal\tAverage')
print('Months\tRain\tRain')
print('-------------------------------')
print(format(numOfMonths, '.1f'),'\t',format(totalInches, '.1f'),'\t',format(avgRainfall, '.1f'))
       
                 
