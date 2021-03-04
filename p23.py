sum=1
for i in range(1,4):
    for j in range(1,4):
        if(j<=3-i):
            print(" ",end="")
        else:
          
            print(sum,sep=" ",end="")
            sum+=1
    print()
   
            
             
