#A set is a collection which is unordered and unindexed.
# In Python, sets are written with curly brackets.
#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Loop through the set, and print the values:
for x in thisset:
  print(x)

#Add an item to a set, using the add() method:
thisset.add("orange")
print(thisset)

#Add multiple items to a set, using the update() method:
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Remove "banana" by using the remove() method:
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:
thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana")
print(thisset1)

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Set intersection() Method
#Return a set that contains the items that exist in both set x, and set y:
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
z1 = x1.intersection(y1)
print(z1)

# issubset() Method
#Return True if all items set x are present in set y:
x2 = {"a", "b", "c"}
y2 = {"f", "e", "d", "c", "b", "a"}
z2 = x2.issubset(y2)
print(z2)

#difference() Method
#Return a set that contains the items that only exist in set x, and not in set y:
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
z3 = x3.difference(y3)
print(z3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)