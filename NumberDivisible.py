#This program verifies if a number is divisible by 2, 3 or both
num = int(input ("Ingress the number to verify: "))

divisibleBy2 = num % 2 == 0
divisibleBy3 = num % 3 == 0

if divisibleBy2 and divisibleBy3: 
    print ("The number ", num, " is divisible by 2 and 3")
elif divisibleBy2:
    print ("The number", num, "is divisible by 2")
elif divisibleBy3:
    print ("The number", num, "is divisible by 3")
else:
    print ("The number", num, "is not divisible by 2 or 3")