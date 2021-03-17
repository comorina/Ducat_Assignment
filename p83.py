d={1:101,2:102,3:103,4:11,5:235}
key=d[1]
for i in range(2,d):
    if(d[i-1]>d[i]):
        temp=d[i-1]
        d[i-1]=d[i]
        d[i-1]=temp
print(d)
        
