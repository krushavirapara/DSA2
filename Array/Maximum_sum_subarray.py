def kadane(nums):
    sum = 0
    maxi = -float('inf')
    for i in range(len(nums)):
        if sum==0:
            start = i

        sum+=nums[i]

        if sum>maxi:
            ansStart = start
            end =i
            maxi  = sum
        if sum<0:
            sum = 0
    return maxi,ansStart,end


print(kadane([-2,1,-3,4,-1,2,1,-5,4]))