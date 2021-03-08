x="India is incredible countory"

word='India'
a=[]
a=x.split(" ")
count=0
for i in range(0,len(a)):
    if(word==a[i]):
        count+=1
print("count: ", count)
