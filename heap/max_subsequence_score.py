#get maximum sum for two arrays

def max_sum(arr1,arr2):
	arr1 = [1,3,3,2]
	arr2 = [2,1,3,4]
	k = 3

	tasks = [(y,x) for x,y in zip(arr1,arr2)]
	tasks.sort()

	
  #to optimize it use reverse descending sort and try to optimize it

	for i in range(len(arr1)-k+1):
		mini = tasks[i][0]
		s = tasks[i][1]
		heap = []
		import heapq
		for j in range(i+1,n):
			heaqp.heappush(heap,(tasks[j][1]))
			if len(heap)>k-1:
				heapq.heappop(heap)
		while heap:
			s+=heapq.heappop(heap)
		res = max(res,(s*mini))
	return res


