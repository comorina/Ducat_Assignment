x=input()
k=x[-1:-4:-1]


if(len(x)>=3):
    if(k=='ing'):
        x=x+'ly'
        print(x)
    else:
        x=x+'ing'
        print(x)
else:
    print(x)
