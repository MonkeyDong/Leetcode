import copy

class Solution:
    def orangesRotting(self, grid):
        lie = len(grid[0])
        hang = len(grid)
        a1 = []
        a2 = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    a2.append((i,j))
                if grid[i][j] == 1:
                    a1.append((i,j))

        def green(x,y):
            tmp = 0
            if x>=0 and x<hang and y>=0 and y<lie and (x,y) in a1:
                a1.remove((x,y))
                a2.append((x,y))
                tmp = 1
            return tmp

        def fun(t):
            tts = 0
            x = t[0]
            y = t[1]
            tts = max(green(x+1,y),tts)
            tts = max(green(x-1,y),tts)
            tts = max(green(x,y-1),tts)
            tts = max(green(x,y+1),tts)
            return tts

        tt = 0
        while(a1 != []):
            arr = a2.copy()
            ss = []
            for i in arr:
                step = fun(i)
                ss.append(step)
            if any(ss):
                tt += 1
            if not any(ss) and a1 != []:
                tt = -1
                break
        return tt

input = [[2],[1]]
leetcode = Solution()
res = leetcode.orangesRotting(input)
print(res)
