#2022-02-05
#5
target_arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(target_arr) + 1)

for i in range(len(target_arr)):
  count[target_arr[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
print()