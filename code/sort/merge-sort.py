def merge(array, start, mid, end):
    i, j, k = start, 0, 0
    
    left_array = array[start:(mid + 1)]
    right_array = array[(mid + 1):(end + 1)]
    print(f"left_array = {left_array}")
    print(f"right_array = {right_array}")
    
    while i <= end:
        print(f"(i, j, k) = ({i}, {j}, {k})")
        if left_array[j] <= right_array[k]:
            array[i] = left_array[j]
            j += 1
            if j >= len(left_array):
                array[i+1:end+1] = right_array[k:len(right_array) + 1]
                break
        else:
            array[i] = right_array[k]
            k += 1
            if k >= len(right_array):
                array[i+1:end+1] = left_array[j:len(left_array) + 1]
                break
        i += 1
    print(f"Exiting merge() with current array = {array}")
    return array


def mergeSort(array, start, end):
    if end - start + 1 <= 1:
        return array
    
    mid = (start + end) // 2
    print(f"Calling mergeSort({array}, {start}, {mid})")
    mergeSort(array, start, mid)
    print(f"Calling mergeSort({array}, {mid + 1}, {end})")
    mergeSort(array, mid + 1, end)
    print(f"Calling merge({array}, {start}, {mid}, {end})")
    merge(array, start, mid, end)
    return array


if __name__ == '__main__':
    array = [3, 2, 4, 1, 6]
    sorted_array = mergeSort(array, 0, len(array) - 1)
    array.sort()
    assert array == sorted_array, "Failed"
    # print(f"original array = {array}")
    # print(f"sorted array = {mergeSort(array, 0, len(array))}")