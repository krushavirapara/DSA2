def slidingMaximum(arr,k):
    i,j=0,0
    max_till_now = []
    ans = []
    while j<len(arr):
        while(max_till_now and max_till_now[-1]<arr[j]):
            max_till_now.pop()
        max_till_now.append(arr[j])
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            ans.append(max_till_now[0])
            if max_till_now == arr[i]:
                max.pop(i)
            i+=1
            j+=1
    return ans

print(slidingMaximum([1, 3, -1, -3, 5, 3, 6, 7],3))

        