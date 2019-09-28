def DFS(list):
    global outlist
    #list为需要全排列的列表
    step = len(outlist)
    # 深度为3
    if step == len(list):
        print(outlist)
        return outlist
    else:
        #flag == 0 means x is on hand
        for index,value in enumerate(list) :
            if value not in outlist:
                outlist.append(value)
                # print(outlist)
                DFS(list)
                #在结束一次递归后返回上一节点，并删除list中的最后一个数
                #画个3叉树理解下，如何从[1,3,3]跳出到[1]
                outlist.pop()

                # print(outlist)

list =[1,2,3]
outlist = []
DFS(list)

