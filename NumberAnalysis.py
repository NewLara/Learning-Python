#Get 20 numbers from user and store in list
#Display lowset, highest, total, and average of the numbers

def main():
    try:
        #get numbers from user
        num_list = getNumbers()

        #print the numbers in list
        printNumbers(num_list)

        #print lowest number
        lowestNum(num_list)

        #print highest number
        highestNum(num_list)

        #print total of all numbers
        totalNum(num_list)

        #print average of all numbers
        avgNum(num_list)
        
    except Exception as err:
        print(err)
    

#*********FUNCTIONS****************
def getNumbers():
    repeat = 10
    #create empty list 
    num_list = [] * repeat

    #while repeat is not 0, get a number and append to list,
    #then decrement repeat
    while repeat != 0:
        num = int(input('Enter a number: '))
        num_list.append(num)
        repeat -= 1

    return num_list

def printNumbers(li):
    print()
    print("The numbers you entered are: " )
    for num in li:
     print(li[num],end ='')
    print()
     

def lowestNum(li):
    low = min(li)
    print('Lowest number in list :', low)
    return min(li)

def highestNum(li):
    high = max(li)
    print('Highest number in list :', high)
    return max(li)

def totalNum(li):
    total = 0.0
    for value in li:
        total += value
    print('The toal of all numbers is:',total)
    return total

def avgNum(li):
    total = totalNum(li)
    avg = total / len(li)
    print('The average of all numbers is:',avg)



main()

    
             
