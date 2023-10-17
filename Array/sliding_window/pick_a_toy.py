#Fruits into basket,maximize toys
#leetcode 904
def pickToys(nums):
    i,j = 0,0
    toys={}
    max_toys=0
    while j<len(nums):
        toys[nums[j]]=toys.get(nums[j],0)+1
        j+=1
        if len(toys)<=2:
            max_toys = max(max_toys,sum(toys.values()))
            #max_toys = max(max_toys,j-i)
        elif len(toys)>2:
            while len(toys)>2:
                toys[nums[i]]-=1
                if toys[nums[i]]==0:
                    toys.pop(nums[i])
                i+=1


    return toys



print(pickToys([1,2,1,3,3,1,2])) #2

