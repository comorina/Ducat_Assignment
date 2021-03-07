#linear Search 
a= [11,23,45,67,78,98,76,54,43,21]
key=67
print("Length of the list : ", len(a))
print("And list is : ",a)
for i in range(len(a)):
    if(a[i]==key):
        print("Index of key = 67 is : ",i)
        break
print("Thanks!")
