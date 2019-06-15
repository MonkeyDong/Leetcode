class Solution:
    def allPathsSourceTarget(self, graph):
        arr = []
        road = [0]
        n = len(graph)
        def fun(road,node):
            if node == []:
                return
            for i in node:
                if i == n-1:
                    road.append(i)
                    arr.append(road)
                    road.pop()
                else:
                    road.append(i)
                    fun(road,graph[i])
            return

        fun(road,graph[0])
        return arr                             
            
arr = [[1,2], [3], [3], []] 
test = Solution()
print(test.allPathsSourceTarget(arr))
