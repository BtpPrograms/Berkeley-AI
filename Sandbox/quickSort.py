originalList = [7, 6, 14, 32, 96, 4, 7, 17, 36, 19]

def quickSort(sortList):
    lesser = []
    same = []
    greater = []
    
    if len(sortList) <= 1:
        return sortList
    else:
        pivot = sortList[0]
        for i in sortList:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                same.append(i)

    return quickSort(lesser) + same + quickSort(greater)

print quickSort(originalList)
