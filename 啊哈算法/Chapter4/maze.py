# DFS中step标记深度，深度必须小于最大格数
# 必须保证走过的格点不能再走，即线路不能重合，考虑未走过的格设为1，走过某格置0，并且初始障碍格就置0
def DFS(outpath, step=0):
    global minstep
    #判断是否结束
    if path_judge(outpath):
        if step < minstep:
            minstep = step
        return minstep
    else:
    #未结束时进行移动，并且移动后需要判断是否合法，未超出边界
        global move
        for x in move:
            outpath[0] += x[0]
            outpath[1] += x[1]
            step += 1
            if outpath[0] in range(5) and outpath[1] in range(4) and graph[outpath[0]][
                outpath[1]] == 1 and step <= minstep:
                # print(outpath)
                graph[outpath[0]][outpath[1]] = 0
                DFS(outpath, step)
                graph[outpath[0]][outpath[1]] = 1
            #进行回溯
            outpath[0] -= x[0]
            outpath[1] -= x[1]
            step -= 1
        #最终该程序最后返回最小步数
        return minstep

def path_judge(path):
    #判断是否到达终点
    if path[0] == 3 and path[1] == 2:
        return True
    else:
        return False


def BFS(outpath,step = 0):
    #stepadd 为在BFS中增加的个数，需要在每一次迭代过程中先减去上一次的搜索结果
    stepadd = 0
    tempoutpath = []

    for everypath in outpath:
        if path_judge(everypath):
            global minstep
            if step < minstep:
                minstep = step
            return minstep
    else:
        #thispath 形如[2,1]，step形如[1,0]
        for thispath in outpath:
            for stepmove in move:
                if canmove(thispath,stepmove,graph):
                    temp = canmove(thispath,stepmove,graph)
                    graph[temp[0]][temp[1]] = 0
                    tempoutpath.append(temp)
                    #
                    stepadd+=1
        #保留刚新增的步骤个数
        #这里采用outpath来保存下一步的坐标，相比于原题的范例代码，没有用队列的数据结构，而是每次给下一步所有可能的抵达位置赋值，这两种都可以，因为哪怕使用队列，也是无法直观看清步骤
        outpath = tempoutpath
        step += 1
        BFS(outpath,step)
        print("step:",step,"path:",outpath)
        return step

def canmove(this,move,map):
    nextmove=[this[0]+move[0],this[1]+move[1]]
    if nextmove[0] in range(len(map)) and nextmove[1] in range((len(map[0]))) and map[nextmove[0]][
        nextmove[1]] == 1:
        return nextmove
    else:
        return False

graph = [[1 for _ in range(4)] for _ in range(5)]
graph[0][0], graph[0][2], graph[2][2], graph[3][1], graph[4][3] = 0, 0, 0, 0, 0
oripath = [[0, 0]]
oristep, condition = 0, 0
move = [[-1, 0], [0, -1], [1, 0], [0, 1]]
minstep = len(graph) * len(graph[0])
#输出深度优先算法寻找的步骤
# print(DFS(oripath, oristep))
print(BFS(oripath, oristep))