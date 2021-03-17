def f(x=3):
    if(x in [0,1]):
        return x
    else:
        print(x,end='')
       return f(x-1)+f(x-2)
n=f()
print(n)
        
