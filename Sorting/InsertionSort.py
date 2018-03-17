def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]   # Desplaza hacia la derecha el valor
            j -= 1
        # print("arr: {} key: {}".format(arr, key))
        arr[j+1] = key


arr = [2,3,5,4,0,5,-2,10,3]
print(arr)
insertion_sort(arr)
print(arr)

