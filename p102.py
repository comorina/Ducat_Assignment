def divide(l):
    if(len(l)>2):
      mid=len(l)//2
      if(len(l)==1):
          pass
      left=l[0:mid]
      right=l[mid:]
    print('left : ',left)
    print('right : ',right)
    return divide(left)
l=[1,2,3,4,5,6,7,8,9,10]

x=divide()
print(x)
