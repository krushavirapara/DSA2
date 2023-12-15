#when largest then min heap
#when "smallest" the "max heap"

import heapq
def kth_smallest(arr,k):

	#brute force would be to sort the array and get the required smallest element
	max_heap = []
	heapq.heapify(max_heap)
	for i in arr:
		
		heapq.heappush(max_heap,-i)
		if len(max_heap)>k:
			heapq.heappop(max_heap)
		

	return -max_heap[0]

print("kth smallest",kth_smallest([1,2,131,4,5,7],3))



#function to get k largest elements from arr
def k_largest(arr,k):
	min_heap=[]
	heapq.heapify(min_heap)
	for i in arr:
		heapq.heappush(min_heap,i)
		if len(min_heap)>k:
			heapq.heappop(min_heap)
	return min_heap

print("k_largest_elements:",k_largest([1,5,4,23,1,323,56],3))

def sum_between_k1_smallest_and_k2_smallest(arr,k1,k2):
	k1_smallest=kth_smallest(arr,k1)
	k2_smallest=kth_smallest(arr,k2)

	ans =0
	for ele in arr:
		if ele>k1_smallest and ele<k2_smallest:
			ans+=ele
	return ans
print(sum_between_k1_smallest_and_k2_smallest([1,3,5,7,11,12],2,6))