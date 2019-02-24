def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


def switch(array, element, pivot):
    pivot_val = array[pivot]
    array[pivot] = array[element]
    array[element] = array[pivot - 1]
    array[pivot - 1] = pivot_val
    return 0, pivot - 1

def quicksort(array):
    if(len(array) <= 1):
        return array
    pivot = len(array)-1
    element = 0
    array1 = []
    array2 = []
    while element < pivot :
        if(array[element] > array[pivot]):
            element, pivot = switch(array, element, pivot)
        else:
            element += 1
    array1 = quicksort(array[0:pivot])
    array2 = quicksort(array[pivot + 1:])
    return array1 + [array[pivot]] + array2

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
