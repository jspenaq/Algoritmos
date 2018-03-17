def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    n, m = 0, 0

    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result


arr = [2,3,5,4,0,5,-2,10,3]
print(arr)
s_arr = merge_sort(arr)
print(s_arr)
