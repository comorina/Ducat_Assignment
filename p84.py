l =[[12,32,34],[45,54,56],[65,67,76]]
for i,j,k in l:
    print(i,j,k)
print()
l=[1,2,3]
a,b,c=l
print(type(a))
print(type(b))
print(type(c))
#=============================================
print()
l=[1,2,3]
t=(10,20,30,40)
s={'a','b','c'}
for i in zip(l,t,s):
    print(i)
print()
for i,j,k in zip(l,t,s):
    print(i,j,k)
    sum=j+i
print(sum)
