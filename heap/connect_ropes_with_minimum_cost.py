import heapq
def connect_ropes_with_minimum_cost(arr):
	min_heap=[]
	heapq.heapify(min_heap)
	total_cost=0

	for rope in arr:
		heapq.heappush(min_heap,rope)

	while len(min_heap)>=2:
		first = heapq.heappop(min_heap)
		second  = heapq.heappop(min_heap)
		total_cost+=first+second
		heapq.heappush(min_heap,first+second)
	return total_cost

print(connect_ropes_with_minimum_cost([1,2,3,4,5,6]))