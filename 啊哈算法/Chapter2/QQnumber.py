def decode(list):
    outputlist = []
    while list:
        pop = list.pop(0)
        if list:
            temp = list.pop(0)
            list.append(temp)
        outputlist.append(pop)
    return outputlist

inputlist = [6,3,1,7,5,8,9,2,4]
#need output [6,7,2,8,1,1,3,4,0]
print(decode(inputlist))