# A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#One item tuple, remember the commma:
thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))

