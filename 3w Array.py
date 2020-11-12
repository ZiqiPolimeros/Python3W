#An array is a special variable, which can hold more than one value at a time.

#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]

#Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

#Add one more element to the cars array:
cars.append("Honda")

#Delete the second element of the cars array:
cars.pop(1)

#Delete the element that has the value "Volvo":
#cars.remove("Volvo")

#Sorts the list
cars.sort()
print(cars)

#Sort the list by the length of the values:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

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
print(cars)