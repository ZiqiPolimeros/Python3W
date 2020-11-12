#List
#A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Print the second item of the list:
print(thislist[1])

#Print the last item of the list:
print(thislist[-1])

#Return the third, fourth, and fifth item:
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])

#This example returns the items from the beginning to "orange":
print(thislist2[:4])

#This example returns the items from "cherry" and to the end:
print(thislist2[2:])

#This example returns the items from index -4 (included) to index -1 (excluded)
print(thislist2[-4:-1])

#To change the value of a specific item, refer to the index number:
thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = "blackcurrant"
print(thislist1)

#You can loop through the list items by using a for loop:
thislist3 = ["apple", "banana", "cherry"]
for x in thislist3:
  print(x)

#Check if "apple" is present in the list:
if "apple" in thislist3:
  print("Yes, 'apple' is in the fruits list")

#Print the number of items in the list:
  print(len(thislist))

#Using the append() method to append an item:
  thislist3.append("orange")
  print(thislist3)

#Insert an item as the second position:
  thislist3.insert(1, "orange")
  print(thislist3)

#The remove() method removes the specified item:
  thislist3.remove("banana")
  print(thislist3)

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist4 = ["apple", "banana", "cherry"]
thislist4.pop()
print(thislist4)

#The del keyword removes the specified index:
thislist5 = ["apple", "banana", "cherry"]
del thislist5[0]
print(thislist5)

#The del keyword can also delete the list completely:
thislist6 = ["apple", "banana", "cherry"]
del thislist6

#The clear() method empties the list:
thislist7 = ["apple", "banana", "cherry"]
thislist7.clear()
print(thislist7)

#Make a copy of a list with the copy() method:
thislist8 = ["apple", "banana", "cherry"]
mylist = thislist8.copy()
print(mylist)

#Make a copy of a list with the list() method:
mylist1 = list(thislist8)
print(mylist1)

#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Append list2 into list1:
for x in list2:
  list1.append(x)
print(list1)

#Use the extend() method to add list2 at the end of list1:
list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]
list4.extend(list5)
print(list4)

#Using the list() constructor to make a List:
thislist9 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist9)

# list.count(value)
# Return the number of times the value 9 appears int the list:
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)
print(max(fruits))
print(min(fruits))


#Reverse the order of the fruit list:
fruits1 = ['apple', 'banana', 'cherry']
fruits1.reverse()
print(fruits)

#List sort() Method
#Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#Sort the list descending:
cars1 = ['Ford', 'BMW', 'Volvo']
cars1.sort(reverse=True)
print(cars1)

#Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars2 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars2.sort(key=myFunc)
print(cars2)

#Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc1(e):
  return len(e)
cars3 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars3.sort(reverse=True, key=myFunc1)
print(cars3)


