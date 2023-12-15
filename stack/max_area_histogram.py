def max_area_histogram(arr):
    def nle(arr):

        v = []
        s = []
        for i in range(len(arr)):
            if len(s) == 0:
                v.append(-1)
            elif s and s[-1][0] < arr[i]:
                v.append(s[-1][1])
            elif s and s[-1][0] >= arr[i]:
                while s and s[-1][0] >= arr[i]:
                    s.pop()
                if len(s) == 0:
                    v.append(-1)
                else:
                    v.append(s[-1][1])
            s.append((arr[i], i))
        return v


    def gle(arr):
        v = []
        s = []

        # Iterate through the array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            if len(s) == 0:
                v.append(len(arr))
            elif s and s[-1][0] < arr[i]:
                v.append(s[-1][1])
            elif s and s[-1][0] >= arr[i]:
                while s and s[-1][0] >= arr[i]:
                    s.pop()
                if len(s) == 0:
                    v.append(len(arr))
                else:
                    v.append(s[-1][1])
            s.append((arr[i], i))

        # Reverse the list to get the correct order
        v.reverse()

        return v


    left = nle(arr)
    right = gle(arr)

    ans = []
    for i in range(len(arr)):
        width = right[i] - left[i] - 1
        ans.append(width * arr[i])

    return max(ans)

print(max_area_histogram([6, 2, 5, 4, 5, 1, 6]))
