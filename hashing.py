def countFrequency(arr,max_length):
    n= [0 for i in range(max_length+1)]

    for i in arr:
        n[i]+=1
    return n

print(countFrequency([1,2,3,5,1,6,7,9],9))

def get_high_low_frequencies(arr): #or you can use dictionaries(hashmap)
    n=[0 for i in range(max(arr)+1)]

    for i in arr:
        n[i]+=1

    return n.index(max(n)),n.index(min(n))

print(get_high_low_frequencies([1,2,3,1,1,4,6,7,8]))