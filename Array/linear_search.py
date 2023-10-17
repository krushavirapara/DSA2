def linear_search(arr,num):
    if num in arr:
        return arr.index(num)
    else:
        return -1

print(linear_search([1,2,3,3,4,5,6],1))