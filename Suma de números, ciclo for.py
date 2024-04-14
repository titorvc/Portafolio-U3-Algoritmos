print ("This program add the first natural numbers until it reachs a limit defined by the user: ")
n = input ("Until what number do you want to sum? ")
n = int (n)

total = 0
for i in range (1, n+1):
    total += i    

print ("The sum is: ", total)
