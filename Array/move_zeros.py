#1.Naive 
# def moveZeroes(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     count = []
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             count.append(nums[i])

#     for i in range(len(count)):
#         nums[i] = count[i]

#     for i in range(len(count), len(nums)):
#         nums[i] = 0


#2.Optiaml
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j=0
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i 
            break
    for i in range(j+1,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            j+=1

nums=[0,12,0,2,1,0,00]
nums2=[1,0,4,5,0,6]
moveZeroes(nums)
print(nums)


