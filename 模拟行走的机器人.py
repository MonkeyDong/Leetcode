class Solution:
    def robotSim(self, commands, obstacles):
        def sums(x,y):
            return [x[0] + y[0], x[1] + y[1]]
        def muls(x,s):
            return [x[0]*s,x[1]*s]
        def tars(n):
            return n[0]*n[0] + n[1]*n[1]
        def f_next(n):
            arr = [[1,0],[0,1],[-1,0],[0,-1]]
            i = 0
            while(1):
                yield arr[(i%4)]
                i += n
        left = f_next(-1)
        right = f_next(1)
        vvs = next(left)
        vvs = next(right)
        mm = 0
        now = [0,0]
        for i in commands:
            if i == -2:
                vvs = next(left)
            if i == -1:
                vvs = next(right)
            if i > 0:
                step = [sums(now,muls(vvs,x)) for x in range(1,i+1)]
                for j in step:
                    if j in obstacles:
                        now = j
                now = step[-1]
                mm = max(tars(now),mm)
        return mm

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]

a = Solution()
res = a.robotSim(commands,obstacles)
print(res) #err
