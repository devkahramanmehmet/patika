newArray = [3, 5, 9, 2, 6, 19]

def insertion_sort(newArray):
    '''Applies insertion sort algorithm on a given unsorted array.'''
    for i in range(1, len(newArray)):
        key_item = newArray[i]
        j = i - 1
        while j >= 0 and newArray[j] > key_item:
            newArray[j + 1] = newArray[j]
            j -= 1
            newArray[j + 1] = key_item
        return newArray
insertion_sort(newArray)