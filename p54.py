''' Write a Python program to swap comma and dot in a string.  
Sample string: "32.054,23"
Expected Output: "32,054.23" '''


x="32.054,23"
str=''
for i in x:
        if(i=='.'):
            temp=i
            i=','
        elif(i==','):
            temp=i
            i='.'
        str+=i
print(str)
            
