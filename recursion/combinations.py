from typing import List


class Combinations:
	#combination 3
	def helper(self,i,k,n,op,ans):
	        if n==0 and k==0:
	            ans.append(op)
	            return ans
	        if k<0 or n<0:
	            return 
	        else:
	            for i in range(i,10):
	                self.helper(i+1,k-1,n-i,op+[i],ans)
	            return ans
	def combinationSum3(self, k: int, n: int) -> List[List[int]]:
	        return self.helper(1,k,n,[],[])

	#combination 2
	def helper2(self,index,target,candidates,op,ans):
        if target==0:
            ans.append(op)
            return ans
        if target<0 and index>len(candidates):
            return 
        else:
            for i in range(index,len(candidates)):
                if candidates[i]>target:
                    return ans
                if i > index and candidates[i-1]==candidates[i]:
                    continue
                self.helper2(i+1,target-candidates[i],candidates,op+[candidates[i]],ans)
            return ans
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        return self.helper2(0,target,sorted(candidates),[],[])

    #combination 1 same as coin change

