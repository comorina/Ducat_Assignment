n = int(input("Enter the number for factorial : "))
fact=1
for i in range(1,n+1):
    fact = fact*i
print("Factorial of {0} : {1}".format(n, fact))    
