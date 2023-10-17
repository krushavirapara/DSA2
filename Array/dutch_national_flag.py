def zeros_and_ones(arr):
    low = 0
    high = len(arr)-1
    while low<=high:
        if arr[low]<0:
            low+=1
        else:
            arr[low],arr[high] = arr[high],arr[low]
            high-=1

arr = [1,0,1,1,0,0,1,1,0,0,0]

zeros_and_ones(arr)
print(arr)
 

def zero_one_two(arr):
    low,mid=0,0
    high = len(arr)-1

    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1

arr = [0,1,2,1,2,0,0,1,0,2,2,0]
pos_neg = [12,-11,-13,-5,6,5,-7,3]
zeros_and_ones(pos_neg)
print(pos_neg)
zero_one_two(arr)
print(arr)
