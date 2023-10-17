def find_union(arr1,arr2):
    hash = []
    for i in arr1:
        if i not in hash:
            hash.append(i)
    for i in arr2:
        if i not in hash:
            hash.append(i)

    return hash
print(find_union([1,2,3,3,3,4],[2,3,4,5,6,1]))