#Identification - repetataive work
#SubarraY having window size
#this is fixed window size

def max_sum_of_subarray_having_size_k(arr,k):
    i,j,sum,mx_sum=0,0,0,0
    while j<len(arr):
        sum+=arr[j]
        if j-i+1<k:
            j+=1
        else:
            mx_sum = max(mx_sum,sum)
            sum = sum - arr[i]
            i+=1
            j+=1

    return mx_sum


print(max_sum_of_subarray_having_size_k([2,5,1,8,2,9,1],3))

#brute force
def max_sum_of_subarray_having_size_k(arr,k):
    mx_sum=0
    for i in range(len(arr)-k):
        sum =0
        for j in range(i,i+3):
            sum+=arr[j]
        mx_sum = max(sum,mx_sum)
    return mx_sum

print(max_sum_of_subarray_having_size_k([2,5,1,8,2,9,1],3))

           