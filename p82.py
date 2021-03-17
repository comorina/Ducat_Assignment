d={101:'Shivam',102:'Vivek',101:'Manish'}
di={'Shivam':101,'Vivek':102,'Manish':101}
print(d)
print(di)
#del d[101]
print(d)
#d.popitem()
#print(d[101])
print(d.get(101,'hdhd'))
print(d)
print()
print(d.values())
print(d.items())
print()
for i in d.values():
    print(i*2)
s={0:[1,2,3],1:[4,5,6]}
print(s)
print(s.get(0,[0]))

r={1,2,3,4}
s=r.clear()
print(type(r))
print(type(s))



#----------------------------------------------

#dict={}
#for i in range(5):
 #   dict[i]=input()
#print(dict)
w={1,2,3}
g=[4,5,6]
h=w.union(g)
print(h)

..


