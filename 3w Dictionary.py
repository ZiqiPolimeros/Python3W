# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Get the value of the "model" key:
x = thisdict["model"]
print(x)

#get() Method
#Get the value of the "model" item:
x1 = thisdict.get("model")
print(x1)

#Change the "year" to 2018:
thisdict["year"] = 2018
print(thisdict)

#Print all key names in the dictionary, one by one:
for x2 in thisdict:
  print(x2)

#Return the keys:
x = thisdict.keys()
print(x)


#Print all values in the dictionary, one by one:
for x3 in thisdict:
  print(thisdict[x3]) #the same result as values() method

#You can also use the values() method to return values of a dictionary:
for x4 in thisdict.values():
  print(x4)

#Loop through both keys and values, by using the items() method:
for x5, y5 in thisdict.items():
  print(x5, y5)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)

#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)



#The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)

#The del keyword can also delete the dictionary completely:

#del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.clear()
print(thisdict)

#Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict)

#Create three dictionaries, then create one dictionary
# that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#It is also possible to use the dict() constructor to make a new dictionary:
thisdict3 = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict3)

#Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)