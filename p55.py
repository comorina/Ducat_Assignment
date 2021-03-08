x=input('Enter text : ')
x=x.lower()
count=0
for i in x:
    if(i=='a'or i=='e' or i=='i' or i=='o' or  i=='u'):
        count+=1
print("Vowel are : ",count)
        
        
