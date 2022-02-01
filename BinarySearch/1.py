#2022-02-01
#1
def binary_search(array, target, start, end):
  while start<=end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

target = int(input("target: "))
print("input array:",end=" ")
arr = list(map(int, input().split()))
arr.sort()

target_idx = binary_search(arr, target, 0, len(arr)-1)
if target_idx == None:
  print("target does not exist")
else:
  print("target %d found at index %d" %(target, target_idx))

