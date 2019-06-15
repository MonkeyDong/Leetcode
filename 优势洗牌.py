'''
class Solution:
    def advantageCount(self,A,B):
        s_a = sorted(B)
        s_b = sorted(A)

        res = []
        for i in s_a:
            for j in range(len(s_b)):
                if s_b[j]>i:
                    res.append(s_b[j])
                    s_b.pop(j)
                    break
        ok = res+s_b

        q = []
        for n in B:
            m = s_a.index(n)
            q.append(ok[m])
        return q


A = [12,24,8,32]
B = [13,25,32,11]

test = Solution()
s = test.advantageCount(A,B)
print(s)
'''
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(A)
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))
        #遍历排过序后的A，B，从A最小的开始，如果可以干对应位置的B，就append进res
        #如果干不过，就让他去匹配B中最强的，废掉B中最强的那个
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res