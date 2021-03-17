def polindrom(l):
    s=str(l)
    if(l==int(s[-1::-1])):
       print('This is polindrom')
    else:
        print('Not Polindrom')
polindrom(int(input()))

