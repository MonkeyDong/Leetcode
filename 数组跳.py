arr = [2,3,1,1,4]

def solution(arr):
	step = 0
	begin = 0
	end = 0
	n = len(arr)
	while(end < n-1):
		max_pos = 0
		for i in range(begin,step):
			max_pos = max(max_pos,i+arr[i])
		begin = end + 1
		end = max_pos
		step += 1
	return step

print(solution(arr))

def booljump(arr):
	n = len(arr)
	left = 0
	right = 0
	while(right < n-1):
		max_pos = right
		for i in range(n):
			max_pos = max(max_pos,arr[i]+i)
		if max_pos < right:
			return False
		left = right
		right = max_pos
	return True

print(booljump(arr))