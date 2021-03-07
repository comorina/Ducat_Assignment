n=int(input())
coef = 1
for i in range(0,n):
    for space in range(1,n-i):
        print(" ",end="")
    for j in range(0,i+1):
        
        print("*",end=" ")
    print()
        
