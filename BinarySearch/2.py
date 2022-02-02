#2022-02-02
#2
def binary_search(arr, target, start, end):
  while start<=end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

arr = [10, 7, 11, 3, 6,17, 21, 9, 12]
arr.sort()
print(arr)
target = 17
idx = binary_search(arr, target, 0, len(arr)-1)
if idx == None:
  print("Target not found")
else:
  print("Target %d found at idx %d" %(target, idx))