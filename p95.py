def armstrong(n):
    num=n
    a=[]
    sum=0
    for i in range(len(str(n))):
        re=n%10
        a.append(re)
        n=n//10
    for i in a:
        sum=sum+i**len(str(num))
    if(sum==num):
       print('Armstrong number')
    else:
       print('Not Armstrong number',)
n=int(input('Enter number : '))
armstrong(n)
