#sum() Function

#Add all items in a tuple, and return the result:
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)

#Start with the number 7, and add all the items in a tuple to this number:

x = sum(a, 7)
print(x)

#min() Function

#Return the name with the lowest value, ordered alphabetically:

x = min("Mike", "John", "Vicky")

#Return the item in a tuple with the lowest value:

a = (1, 5, 3, 9)
x = min(a)

# Python prog to illustrate the following in a list

def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length - 1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length - 2])
    print("Second Smallest element is:", list1[1])

# Driver Code
list1 = [22, 85, 62, 40, 55, 12, 39, 2, 43]
find_len(list1)


# Python program to find largest, smallest,
# second largest and second smallest in a
# list with complexity O(n)
def Range(list1):
    largest = list1[0]
    lowest = list1[0]
    largest2 = None
    lowest2 = None
    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 == None or lowest2 > item:
            lowest2 = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)


# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)


# Swap function
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))

## Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):

    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list

# Driver function
List = [12, 65, 91, 90]
pos1, pos2  = 1, 3

print(swapPositions(List, pos1-1, pos2-1))
