def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print("i:", i)
        for j in range(n-i-1):
            print("j:", j)
            if arr[j] > arr[j+1]:
                print("Antes del swap: {}".format(arr))
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
                print("Despues del swap: {}".format(arr))
    return arr


arr = [2,3,5,4,0,5,-2,10,3]
print(arr)
bubble_sort(arr)
print(arr)
