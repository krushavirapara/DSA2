import heapq
def top_k_frequent_elements(arr,k):
	min_heap =[]
	heapq.heapify(min_heap)

	frequency_map={}

	for i in arr:
		if i not in frequency_map:
			frequency_map[i]=1
		else:
			frequency_map[i]+=1

	for ele in frequency_map:
		heapq.heappush(min_heap,[frequency_map[ele],ele])

		if len(min_heap)>k:
			heapq.heappop(min_heap)
	res=[]
	for i in min_heap:
		res.append(i[1])
	return res

print(top_k_frequent_elements([1,1,1,1,2,3,2,2,4,3],k=3))

#sort elements according to frequency
def frequency_sort(arr):
	max_heap =[]
	heapq.heapify(max_heap)

	frequency_map={}

	for i in arr:
		if i not in frequency_map:
			frequency_map[i]=1
		else:
			frequency_map[i]+=1

	for ele in frequency_map:
		heapq.heappush(max_heap,[-frequency_map[ele],ele])

	res =[]
	while max_heap:
		top_frequency = heapq.heappop(max_heap)
		top_frequency[0]= -top_frequency[0]


		for i in range(top_frequency[0]):
			res.append(top_frequency[1])
	return res


print(frequency_sort([1,2,2,2,2,2,3,3,4]))





