for i in range(1,5):
    space= 2*4-2*i
    for j in range(1,i+1):
        print("*",end=" ")   
    for j in range(space+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    space= 2*4-2*i
    for j in range(1,i+1):
        print("*",end=" ")   
    for j in range(space+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

