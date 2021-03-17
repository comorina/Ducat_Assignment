a=input("enter strings: ").strip()
b=list(a.split(' '))
c=set(a.split(' '))
for i in c:
    str1=b.count(i)
    print(i + " : " +str(str1))
    
