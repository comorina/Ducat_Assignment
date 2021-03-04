a= int(input("Enter 1st number : "))
b= int(input("Enter 2nd number : "))
ch = int(input("Enter your choice : \n 1. add, \2.subtraction, \n3.division, \4. multiplication, \5. find inverse, \n6.cube : "))
if(ch==1):
    print("Addition of two number : ",a+b)
elif(ch==2):
    print("Subtraction of two number : ",a-b)
elif(ch==3):
    print("Division of two number : ",a/b)
elif(ch==4):
    print("Multiplication of two number : ",a*b)
elif(ch==5):
    print("Inverse of 1st number : ",1/a)
    print("Inverse of 2nd number : ",1/b)
elif(ch==6):
    print("Cube of 1st number", a**3)
    print("Cube of 2nd number", a**3)
else:
    print("invalid choice")
