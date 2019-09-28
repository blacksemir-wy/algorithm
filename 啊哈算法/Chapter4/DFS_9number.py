def DFS(list):
    if len(outlist) == len(list) and calculate(outlist):
        print(outlist[:3],"+",outlist[3:6],"=",outlist[-3:])
        return outlist
    else:
        for x in list:
            if x not in outlist:
                # print(outlist)
                outlist.append(x)
                DFS(list)
                outlist.pop()


def calculate(array):
    number1 = array[0] * 100 + array[1] * 10 + array[2]
    number2 = array[3] * 100 + array[4] * 10 + array[5]
    number3 = array[6] * 100 + array[7] * 10 + array[8]
    while number1 + number2 == number3:
        return True
    else:
        return False


list = [x for x in range(1, 10)]
outlist = []
# print(calculate([1,2,3,4,5,6,5,7,9]))
DFS(list)
