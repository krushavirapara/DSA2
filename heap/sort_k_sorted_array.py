import heapq
def sort_k_ssorted_array(arr,k):
	# min_heap =[]
	# heapq.heapify(min_heap)
	# for i in arr:
	# 	heapq.heappush(min_heap,i)

	# i=0
	# while min_heap:
	# 	arr[i]=heapq.heappop(min_heap)
	# 	i+=1
	# return arr

	#more space efficient
	min_heap=arr[:k+1]
	heapq.heapify(min_heap)

	ind =0
	for i in arr[k+1:]:
		arr[ind]=heapq.heappop(min_heap)
		heapq.heappush(min_heap,i)
		ind+=1
	while min_heap:
		arr[ind]=heapq.heappop(min_heap)
		ind+=1
	return arr



print(sort_k_ssorted_array([6, 5, 3, 2, 8, 10, 9],3))




	

