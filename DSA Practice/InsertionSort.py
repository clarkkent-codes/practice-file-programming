def insertionSort(array, size):    
    for i in range(1, size):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
                
    print("Insertion Sort:",array)

array = [5, 310, 30, 31, 23, 25]
size = len(array)
insertionSort(array, size)