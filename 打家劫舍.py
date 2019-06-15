nums = [2,7,9,3,1]
c = 0

#贪心false
'''

def fun(nums):
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		if nums[0] > nums[1]:
			global c
			c = 0
			return nums[0]
		if nums[1] > nums[0]:
			global c
			c = 1
			return nums[1]
	if len(nums) > 2:
		dp = fun(nums[:2])
		if c == 0:
			return dp + fun(nums[2:])
		if c == 1:
			return dp + fun(nums[3:])


'''


#动规true
'''
def rob(nums):
	n =len(nums)
	dp = []
	if n == 0:
		return 0
	if n == 1:
		return nums[0]
	if n == 2:
		return max(nums[0],nums[1])
	dp[0] = nums[0]
	dp[1] = max(nums[0],nums[1])
	for i in range(2,n):
		dp[i] = max(nums[i] + dp[i-2],dp[i-1])
	return dp[n-1]
'''
############################################

def fun(nums):
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		if nums[0] > nums[1]:
			return nums[0]
		if nums[1] > nums[0]:
			return nums[1]
	if len(nums) > 2:
		n1 = nums[0]
		n2 = nums[1]
		for i in range(2,len(nums)):
			t = max(n1+nums[i],n2)
			n1 = n2
			n2 = t
	return n2


result = fun(nums)
print(result)







