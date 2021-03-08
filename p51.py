x='shivam'
a=[]
str=''
for i in x:
    a.append(i)
pos=int(input('enter the position :'))
a.insert(pos, a[-1])
a.pop()
print(str.join(a))
