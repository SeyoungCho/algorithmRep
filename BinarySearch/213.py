#2023-05-30
#213
arr = [10, 7, 11, 3, 6, 17, 21, 9, 12]


def binary_search(arr, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if arr[mid] == target:
			return mid
		if arr[mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	return None


arr.sort()
target = 17
idx = binary_search(arr, target, 0, len(arr) - 1)
if idx == None:
	print(f"Target {target} not found")
else:
	print(f"Target {target} found at idx {idx}")
