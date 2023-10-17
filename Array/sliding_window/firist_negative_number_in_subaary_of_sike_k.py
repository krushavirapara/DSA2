#Identification - subarray of size k 


def printFirstNegativeInteger(arr,k):
    i,j=0,0
    sl = []
    ans = []
    while(j<len(arr)):
        if arr[j]<0:
            sl.append(arr[j])
        if j-i+1<k:
            j+=1
        elif j-i+1 == k:
            if sl:
                ans.append(sl[0])
                if sl[0]==arr[i]:
                    sl.pop(0)   
            else:
                ans.append(0)
            i+=1
            j+=1

    return ans

print(printFirstNegativeInteger([-8, 2, 3, -6, 10],2))