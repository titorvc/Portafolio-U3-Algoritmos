print ("This program determines if a program has 1 digit, is negative or positive")
x = input ("Digit a number: ")
x = int (x)

if x<9 and x>0:
    print ("Your number is a unit")

if x<0:
    print ("Your number is negative")

if x>9:
    print ("Your number is bigger than 9 and is positive")