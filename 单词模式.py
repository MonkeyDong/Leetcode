pattern = 'abba'
str = 'dog cat cat dog'


class Solution:
    def wordPattern(self, pattern, str):
        str = str.split(" ")
        dic = {}
        val = []
        for i,j in zip(pattern,str):
            if not (i in dic.keys() or j in val):
                dic[i] = j
                val.append(j)
            if i in dic.keys():
                if dic[i] == j:
                    print(dic[i]+'='+j)
                    continue
                else:
                    return False
        return True


a = Solution()
res = a.wordPattern(pattern,str)
print(res)


