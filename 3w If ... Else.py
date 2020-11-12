
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

#One line if else statement:
a1 = 2
b1 = 330
print("A") if a1 > b1 else print("B")

#And
#The and keyword is a logical operator, and is used to combine conditional statements:
a2 = 200
b2 = 33
c2 = 500
if a2 > b2 and c2 > a2:
  print("Both conditions are True")

#Or
#The or keyword is a logical operator, and is used to combine conditional statements:

if a2 > b2 or a2 > c2:
  print("At least one of the conditions is True")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
a3 = 33
b3 = 200
if b3 > a3:
  pass
