def quickSort(sortList):
    
    lesser = []
    same = []
    greater = []

    if len(sortList) <= 1:
        return sortList
    else:
        pivot = sortList[0]
        lesser = [x for x in sortList if x < pivot]
        same = [x for x in sortList if x == pivot]
        greater = [x for x in sortList if x > pivot]

    return quickSort(lesser) + same + quickSort(greater)

testList = [17, 32, -6, 37, 1, 2, 4, 7, 17, 99, 176.5]

print quickSort(testList)
