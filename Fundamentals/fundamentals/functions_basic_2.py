# 1 - Countdown
def countDown(x):
    countList = []
    for nums in range(x, -1, -1):
        countList.append(nums)
    return(countList)
print(countDown(10))

# 2 - Print and Return
def print_and_return(twoNums):
    print(twoNums[0])
    return(twoNums[1])
print(print_and_return([1, 3]))

# 3 - First Plus Length
def first_plus_length(allNums):
    return allNums[0] + len(allNums)
print(first_plus_length([1, 2, 3, 4, 5]))

#4 - Values Greater than Second
def values_greater_than_second(theseNums):
    newList = []
    if len(theseNums) < 2:
        return False
    for i in theseNums:
        if i > theseNums[1]:
            newList.append(i)
    else:
        print(len(newList))
        return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5 - This Length, That Value
def length_and_value(x,y):
    newestList = []
    for i in range(x):
        newestList.append(y)
    return newestList
print(length_and_value(4,7))
print(length_and_value(6,2))