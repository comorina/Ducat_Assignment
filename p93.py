def primeNumber(n):
    count=0
    for i in range(2,n+1):
        if(n%i==0):
            count+=1
        else:
            continue
    if(count>1):
        print('Not Prime')
    else:
        print('Prime')
primeNumber(int(input('Enter number : ')))
