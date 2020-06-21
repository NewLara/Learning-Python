#read date from user and print in different string format


def main():
            
    date = input("Enter a date in format 'mm/dd/yyy' : ")

    #create date list
    date_list = date.split('/')

    month = date_list[0]
    day = date_list[1]
    year = date_list[2]

    if int(month) > 0 and int(day) > 0 and int(year) > 0 :
        if month == '01':
            month = 'Janurary'
            printNewDate()
        elif month == '02':
            month = 'Feburary'
            printNewDate()
        elif month == '03':
            month = 'March'
            printNewDate()
        elif month == '04':
            month = 'April'
            printNewDate()
        elif month == '05':
            month = 'May'
            printNewDate()
        elif month == '06':
            month = 'June'
            printNewDate()
        elif month == '07':
            month = 'July'
            printNewDate()
        elif month == '08':
            month = 'August'
            printNewDate()
        elif month == '09':
            month = 'September'
            printNewDate()
        elif month == '10':
            month = 'October'
            printNewDate()
        elif month == '11':
            month = 'November'
            printNewDate()
        elif month == '12':
            month = 'December'
            printNewDate()
        else:
            print("This is not a valid Month")
    else:
        print('Enter a valid date') 
def printNewDate():
        print(month + ' ' + day + ',' + year)

main()
