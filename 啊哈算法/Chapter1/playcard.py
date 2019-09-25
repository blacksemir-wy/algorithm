def playcard(lista,listb):
    cardlist = []
    # 两人都有牌情况下a先出牌，一人一张
    while lista and listb:
        #a出牌
        temp = lista.pop(0)
        cardlist.append(temp)
        #对出牌结果判断，findcard()返回出的牌在牌堆的index，该函数返回0则跳过收牌阶段
        if findcard(cardlist,temp):
            listindex=findcard(cardlist, temp)-1
            lista += cardlist[listindex:]
            cardlist = cardlist[:listindex]
        #b出牌
        temp = listb.pop(0)
        cardlist.append(temp)
        #对b出牌结果进行判断
        if findcard(cardlist, temp):
            listindex = findcard(cardlist, temp)-1
            listb += cardlist[listindex:]
            cardlist = cardlist[:listindex]
    if lista:
        print("winner is playerb,left card of playera is:",cardlist,lista)
        return lista
    else:
        print("winner is playera,left card of playera is:",cardlist,listb)
        return listb

def findcard(array,number):
    if number in array[:-1]:
        return array.index(number)+1
    else:
        return 0

lista =[1,5,7,2,3,5]
listb=[2,3,1,5,1,2]
playcard(lista,listb)