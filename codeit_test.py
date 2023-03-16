def sum_digits(nums):
    # 여기에 코드를 작성하세요.
	end = []
	for i in range(len(nums)):
		this_sum = 0
		while nums[i] // 10 != 0:
			this_sum += nums[i] % 10
			nums[i] = nums[i] // 10
		this_sum += nums[i]
		if this_sum % 2 == 0:
			end.append(True)
		else:
			end.append(False)
	return end

def binary_search(element, arr):
	answer = None
	left = 0
	right = len(arr) - 1
	while left <= right:
		middle = (left + right) // 2
		if arr[middle] == element:
			answer = middle
			break
		if arr[middle] < element:
			left = middle + 1
		elif arr[middle] > element:
			right = middle - 1
	return answer

def convert_decimal_to_binary(decimal_num):
	answer = "0b"
	store = []
	while decimal_num // 2 != 0:
		store.append(decimal_num % 2)
		decimal_num = decimal_num // 2
	store.append(decimal_num)
	i = len(store) - 1
	while i >= 0:
		answer += str(store[i])
		i -= 1
	return answer

def convert_decimal_to_binary_first(decimal_num):
	answer = "0b"
	while decimal_num // 2 != 0:
		answer += str(decimal_num % 2)
		decimal_num = decimal_num // 2
	return answer

class User:
	def __init__(self, name, email, password):
		self.name = name
		self.name = email
		self.name = password

def trapping_rain(buildings):
	pass

	
# print(sum_digits([1,2,12,34,44]))
# print(binary_search(8, [1,2,3,4,5]))
# print(convert_decimal_to_binary(10))
# print(convert_decimal_to_binary_first(10))
print(trapping_rain([0, 1, 0, 2, 2, 3, 2, 1, 2]))