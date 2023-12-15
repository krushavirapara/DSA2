import heapq
def k_closest_points_to_origin(arr,k):
	max_heap = []
	heapq.heapify(max_heap)

	for point in arr:
		heapq.heappush(max_heap,[-(point[0]*point[0] + point[1]*point[1]),point])

		if len(max_heap)>k:
			heapq.heappop(max_heap)

	return [point[1] for point in max_heap]

print(k_closest_points_to_origin([[1,3],[-2,2],[5,8],[0,1]],2))