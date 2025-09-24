def selectionSort(array, size):
    for current_num in range(1, size):
        smallest_num = current_num
        for next_num in range(current_num + 1, size):
            if array[next_num] < array[current_num]:
                array[current_num], array[next_num] = array[next_num], array[current_num]

    print("Selection Sort:",array)

    

array = [5, 310, 30, 31, 23, 25]
size = len(array)
selectionSort(array, size)
