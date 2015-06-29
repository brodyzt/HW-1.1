def standardDeviation (list):
    sum = 0.0
    numOfNums = len(list)
    for num in list:
        sum += num
    mean = sum/numOfNums
    tempList = []
    variance = 0.0
    for num in list: #calculates the differences between the numbers and the mean
        tempDifference = num - mean
        tempDifference = tempDifference ** 2
        variance += tempDifference
    variance /= (numOfNums - 1) #calculates the variance
    return variance ** .5 #returns the standard deviation

list = [] #list to store entered numbers to calculate standard deviation


print('This program will ask you to enter a series of numbers and will then'
      ' print the max, min, and mean.\n')
listLength = input("How many numbers do you want to enter?: ") #user enters how many numbers they want to input

#creates the variables used later for calculations
sum = 0.0
max = None
min = None

for x in range(0, listLength):
    print("Enter number")
    tempNum = 0
    tempNum = input() #creates a temporary variable to store the user's input
    list.append(tempNum) #adds entered number to standard deviation list
    if(x == 0): #sets the minimum and maximum to the first number input
        min = tempNum
        max = tempNum
    sum += tempNum #adds the entered number to the runnning total
    if(tempNum > max): #updates the maximum
        max = tempNum
    if(tempNum < min): #updates the minimum
        min = tempNum

#the following prints the calculated values from the entered data
print("\nMax: " + str(max))
print("Min: " + str(min))
print("Mean: " + str(round((sum/listLength), 3)))
print('The standard deviation is: ' + str(round(standardDeviation(list), 3)))
