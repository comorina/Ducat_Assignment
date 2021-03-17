#insertion sort
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
print()
def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>i[j+1]:
                temp=i[j]
                i[j]=i[j+1]
                i[j+1]=temp
                
arr=[12,11,13,5,6]
insertionSort(arr)
bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print("%d"%arr[i],end=",")
