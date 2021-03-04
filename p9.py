hindi = int(input("Enter the number obtain in Hindi : "))
Math = int(input("Enter the number obtain in Math : "))
English = int(input("Enter the number obtain in English : "))
Science = int(input("Enter the number obtain in Science : "))
History = int(input("Enter the number obtain in History : "))


per = ((hindi+Math+English+Science+History)*100//500)

if(per>=60):
    print("First Div")
elif(per>=50 and per<59):
    print("Second Div")
elif(per>=40 and per<49):
    print("Third Div")
else:
    print(per<40)
