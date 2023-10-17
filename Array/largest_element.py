def find_largest(arr):
    if len(arr)==1:
        return arr[0]
    else:
        max=arr[0]
        for i in range(1,len(arr)):
            if max<arr[i]:
                max= arr[i]
        return max

print(find_largest([1,2,3,4,5,6,7,8,9]))

def second_largest(arr):
    max = arr[0]
    sec_max = arr[0]
    for i in range(1,len(arr)):
        if max<arr[i] :
            sec_max = max
            max = arr[i]
        if sec_max<arr[i] and arr[i]!=max:
            sec_max = arr[i]

    return sec_max

print(second_largest([1,3,2,4,6,91,46]))