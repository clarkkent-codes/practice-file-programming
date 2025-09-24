def bubbleSort(array, size):    
    for i in range(size):
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print("Bubble Sort:",array)

array = [5, 310, 30, 31, 23, 25]
size = len(array)
bubbleSort(array, size)
