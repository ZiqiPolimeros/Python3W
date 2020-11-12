# For Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

num = [5,10,0,60]
for i in num:
    try:
        if 600%i == 0:
            print ("{0} is divisible by 600 ".format(i))
        else:
            print("{0} is not divisible by 600 ".format(i))
    except:
        print("{0} can not be denominator".format(i))