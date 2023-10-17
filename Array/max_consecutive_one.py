#Leetcode 485
def findMaxConsecutiveOnes( nums) -> int:
    count=0
    max_one=count
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count=0
        if max_one<count:
                max_one=count
    return max_one


print(findMaxConsecutiveOnes([1,1,0,1,1,1,1]))