def msort(arr):
	'''
	sort the array in place.
	indx = [0,1,2,3,4]
	eg = [5,4,3,1,2]
	'''

	low = 0
	high = len(arr)-1
	return merge_sort(arr)
	


def merge_sort(arr):
	if len(arr)==1:
		return arr
	mid = len(arr)//2
	left =merge_sort(arr[:mid+1])
	right = merge_sort(arr[mid+1:])
	return merge(left,right)

def merge(left,right):
	i = 0
	j = 0
	temp = []
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			temp.append(left[i])
			i+=1
		else:
			temp.append(right[j])
			j+=1
	while i<len(left):
		temp.append(left[i])
		i+=1
	while j<len(right):
		temp.append(right[j])
		j+=1
	return temp


print(msort([5,4,3,2,1]))

