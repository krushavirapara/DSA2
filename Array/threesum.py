def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans=set()
        # n=len(nums)
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k]==0:
        #                 temp=tuple(sorted((nums[i],nums[j],nums[k])))
        #                 ans.add(temp)
        # return list(ans)
        
        # ans = set()
        # n=len(nums)
        # for i in range(n):
        #     hashm = set()
        #     for j in range(i+1,n):
        #         target = -(nums[i]+nums[j])
        #         if target in hashm:
        #             temp=tuple(sorted((nums[i],nums[j],target)))
        #             ans.add(temp)
        #         hashm.add(nums[j])
        # return list(ans)
                
            
        nums.sort()
        res=[]
        
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
                
            l =i+1
            r=len(nums)-1
            
            while l<r:
                three = a+nums[l]+nums[r]
                if three>0:
                    r-=1
                elif three<0:
                    l+=1   
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
                        
                    
                    
                
                    
        