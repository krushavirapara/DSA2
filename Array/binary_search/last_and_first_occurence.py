# first and last occurence of an element 

class Solution:
    def search(self,nums,target,firstIndex):
        start = 0
        end= len(nums)-1
        ans = -1
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid]<target:
                start = mid+1
            elif arr[mid]>target:
                end = mid-1
            else:
                ans = mid
                if(firstIndex):
                    end = mid-1
                else:
                    start = mid+1
        return ans
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        ans[0] = self.search(nums,target,True)
        ans[1] = self.search(nums,target,False)
        return ans
        