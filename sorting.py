def selectionSort(arr): #T.C = O(n^2)
    n=len(arr)
    for i in range(n):
        min = i
        for j in range(i,n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

print(selectionSort([2,5,6,1,3,1]))


def BubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]  = arr[j+1],arr[j]

    return arr

print(BubbleSort([54,2,7,8,1,6]))

def InsertionSort(arr):
    n = len(arr)

    for i in range(1,n):
        j=i
        while(arr[j]<arr[j-1] and j>0):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1

    return arr

print(InsertionSort([12,4,23,56,7,21,1]))


def recurrsiveBubbbleSort(arr,n):
    if n==1:
        return
    else:
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] =  arr[j+1],arr[j]

        recurrsiveBubbbleSort(arr,n-1)

arr=[505,40,303,2,1,45]
recurrsiveBubbbleSort(arr,6)
print(arr)

def recurrsiveINsertionSort(arr,i,n):
    if i==n:
        return
    else:
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1]  = arr[j-1],arr[j]
            j-=1

        recurrsiveINsertionSort(arr,i+1,n)

arr=[10,40,30,1,2,7,8]
recurrsiveINsertionSort(arr,0,7)
print(arr)


def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = [ ]
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right += 1

    while left<=mid:
        temp.append(arr[left])
        left+=1


    while right<=high:
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]


def mergeSort(arr,low,high):
    if(low==high):
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

arr=[2,3,4,5,1,6,2]
mergeSort(arr,0,6)
print(arr)

def quick(arr,low,high):
    pivot = arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1

        while arr[j]>pivot and j>=low+1:
            j-=1

        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]

    arr[low],arr[j] = arr[j],arr[low]
    return j

def quickSort(arr,low,high):
    if low<high:
        breakage = quick(arr,low,high)
        quickSort(arr,low,breakage-1)
        quickSort(arr,breakage+1,high)


n=[5,4,3,2,1,6,7,5,2]
quickSort(n,0,len(n)-1)
print(n)


