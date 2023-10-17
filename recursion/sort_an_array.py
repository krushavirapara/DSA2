def insert(arr,temp):
    if len(arr)==0 or arr[-1]<=temp:
        arr.append(temp)
        return arr
    else:
        last =  arr.pop()
        insert(arr,temp)
        arr.append(last)
        return arr
    

def sort_array(arr):
    if len(arr)==1:
        return 
    else:
        temp = arr.pop()
        sort_array(arr)
        return insert(arr,temp)
 

print(sort_array([1,2,6,7,5,0]))