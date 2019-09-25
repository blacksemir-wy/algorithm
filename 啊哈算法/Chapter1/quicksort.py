def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        left, right = [], []
        pivot = list.pop(0)
        for number in list:
            if number < pivot:
                left.append(number)
            else:
                right.append(number)
        return quicksort(left) + [pivot] + quicksort(right)

testlist = [4, 5, 1, 7, 2]
print(quicksort(testlist))
