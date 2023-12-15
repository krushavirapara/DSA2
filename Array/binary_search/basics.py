#you dont know whether arrays is sorted in ascending or in descending
def orderagnostic_search(arr,target):
	s =0
	e = len(arr)-1
	#check whether ascending or descending
	isAsc = True if arr[s]<=arr[e] else False

	while(s<=e):
		mid = s + (e-s)//2

		if target == arr[mid]:
			return mid
		if isAsc:
			if target>arr[mid]:
				s=mid+1
			elif target<arr[mid]:
				e = mid-1
		else:
			if target>arr[mid]:
				e = mid-1
			elif target<arr[mid]:
				s =mid+1
	return -1

print(orderagnostic_search[17,16,12,11,9,8,7],7)

#smallest element greater than target
def ceiling(nums,target):
	start =0
	end = len(nums)-1
	if target>arr[end]:
		return -1
	while start<=end:
		mid  = start + (end-start)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]<target:
			start = mid+1
		elif arr[mid]>target:
			end  = mid -1
	return start

print(ceiling(2,3,4,7,10,12,14,17),15)


# lagest element greater than target
def floor(nums,target):
	start =0
	end = len(nums)-1
	while start<=end:
		mid  = start + (end-start)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]<target:
			start = mid+1
		elif arr[mid]>target:
			end  = mid -1
	return end

print(floor(2,3,4,7,10,12,14,17),15)





