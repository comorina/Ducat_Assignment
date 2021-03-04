math = int(input("Enter your Math marks : "))
physics = int(input("Enter your Physics : "))
chemistry = int(input("Enter your Chemistry : "))

total = math+physics+chemistry
total2 = math+physics
if(math>=60 and physics>=50 and chemistry>=40) or (total>=200) or (total2>=150):
    print("You can get admission in University")
else:
    print("Sorry!")
