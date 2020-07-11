#function that accepts a list as argument 
# and returns the largest value
#using recusrsion to find largest item 

def main():
    numbers = [299,3,44,55,6,77,34, 120]
    print("the highest number in the list is : ", highestNum(numbers))

def highestNum(numbers):
    #base case, 
    # and will return highest number 
    # when all lower elements are removed
    if len(numbers) == 1:
        return numbers[0]
    #compare 1st to 2nd and keep the highest
    if numbers[0] < numbers[1]:
        numbers.remove(numbers[0])
    else:
        numbers.remove(numbers[1])
    #call function again with the lowest element removed
    return highestNum(numbers)
    
main()
