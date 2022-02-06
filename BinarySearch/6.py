#2022-02-06
#6
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
target_idx= binary_search(arr, target, 0, len(arr)-1)
print(arr)
if target_idx == None:
  print("Target not found")
else:
  print("Target %d found at idx %d"%(target, target_idx))