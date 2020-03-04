def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    greater = []
    lesser = []
    for i in arr:
        if i > pivot:
            greater.append(i)
        else:
            lesser.append(i)
    return quicksort(lesser) + [pivot] + quicksort(greater)
    
