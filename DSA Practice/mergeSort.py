def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        right = array[mid:]
        left = array[:mid]

        mergeSort(right)
        mergeSort(left)

        i = 0
        j = 0
        counter = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[counter] = left[i]
                i += 1
            else:
                array[counter] = right[j]
                j += 1
            counter += 1

        while i < len(left):
            array[counter] = left[i]
            i += 1
            counter += 1
        
        while j < len(right):
            array[counter] = right[j]
            j += 1
            counter += 1 

array = [5, 310, 30, 31, 23, 25]
mergeSort(array)
print("Merge Sort:",array)
