maze=[[1,0,0,1,0,1],
      [1,1,1,0,1,0],
      [0,0,1,0,1,1],
      [0,1,1,1,1,1],
      [0,0,0,1,0,1],
      [1,0,0,1,1,1]]

def vaild(maze,x,y):
    if (x>=0 and y>=0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 1):
        return True
    else:
        return False

def out(maze,x,y):
    #if x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1: 
    if (x == len(maze)-1 and y == len(maze)-1) or (x == 0 and y == 0):
        return True
    else:
        return False


all_ways = []
def walk(maze,x,y,way):
    if vaild(maze,x,y):
        way.append((x,y))
        maze[x][y] = 2
        if not out(maze,x,y):
            #或者用栈实现递归中way的传递
            w1 = way.copy()
            w2 = way.copy()
            w3 = way.copy()
            w4 = way.copy()
            walk(maze,x,y+1,w3)
            walk(maze,x,y-1,w4)
            walk(maze,x+1,y,w1)
            walk(maze,x-1,y,w2)
        else:
            all_ways.append(way)
        maze[x][y] = 1
    return

ways = []
walk(maze,3,1,ways)
for i in all_ways:
    print(i)

