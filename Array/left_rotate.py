#Leetcode 189

#1.Naive Approrach 
# def rotate( nums, k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
    # for i in range(k):
    #     temp = nums[-1]
    #     for j in range(len(nums)-2,-1,-1):
    #             nums[j+1] = nums[j]
    #     nums[0]=temp
    # return nums


#2.better 
# def rotate(nums,k):
#     n= len(nums)
#     k=k%len(nums)
#     nums1 = nums[n-k:n]
#     nums2 = nums[:n-k]
#     temp = nums1 + nums2
    
#     for i in range(len(nums)):
#         nums[i] = temp[i]


#3.Optimal
def reverse(nums,start,end):
    while start<end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1

def rotate(nums,k):
    k=k%len(nums)
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)

    return nums       
            
print(rotate([1,2,3,4,5,6,7],3))