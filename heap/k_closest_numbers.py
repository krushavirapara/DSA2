import heapq

#here we sort according to distance hence key will be difference and we want smallest possible 
#distance hence we use max_heap

def k_closest_numbers(arr,k,x):
	max_heap =[]
	heapq.heapify(max_heap)

	for i in arr:
		heapq.heappush(max_heap,[-abs(i-x),i])
		if len(max_heap)>k:
			heapq.heappop(max_heap)

	res =[]
	while max_heap:
		res.append(heapq.heappop(max_heap)[1])
	return res

print(k_closest_numbers([1,2,5,6,7,8,9,10],3,7))
