def posORneg(x):
    if(x==0 or x== -0 or x== +0):
        print('Not Positive and Not Negative')
    elif(x>0):
        print(x,': Positive')
    else:
        print(x,': Negative')
posORneg(int(input()))
