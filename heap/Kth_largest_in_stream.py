#leetcode 703
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap =[]
        
        for i in range(len(nums)):
           
            if len(self.min_heap)<self.k:
                heapq.heappush(self.min_heap,nums[i])
            else:
                heapq.heappushpop(self.min_heap,nums[i])
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        # Maintain the min heap size to be k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the kth largest element
        return self.min_heap[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)