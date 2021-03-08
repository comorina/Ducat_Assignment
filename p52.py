x=input()
a=[]
for i in x:
    a.append(i)
if(len(a)%4==0):
    a=a[-1::-1]
str=''
print(str.join(a))
