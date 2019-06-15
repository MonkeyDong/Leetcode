S = "a1b2"

class Solution:
	def letterCasePermutation(self, S):
		aa = []
		lists = []
		dic = {}
		for i in S:
			if i.isdigit():
				continue
			if i.isalpha():
				lists.append(i)
				dic[i] = S.index(i)

		arr = [[]]
		for i in range(len(lists)):
			for j in range(i+1,len(lists)+1):
				arr.append(lists[i:j])
				for i in arr:
					ss = S
					for j in i:
						ss = ss[:dic[j]] + j.upper() + ss[(dic[j])+1:]
					aa.append(ss)
		return aa

a = Solution()
a.letterCasePermutation(S)






