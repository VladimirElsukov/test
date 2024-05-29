def is_subarray_equal(arr1, arr2, i):

    return arr1[i:i + len(arr2)] == arr2

def count_subarray_occurrences(arr1, arr2):
    count = 0

    for i in range(len(arr1) - len(arr2) + 1):
        if is_subarray_equal(arr1, arr2, i):
            count += 1
    return count

arr1 = [1, 2, 3, 4, 2, 3, 4, 5, 2, 3, 4, 5, 3, 2, 4, 3, 4, 2, 3, 4, 5, 2, 3, 4, 5, 3, 2, 4]
arr2 = [2, 3, 4]

occurrences = count_subarray_occurrences(arr1, arr2)

print(f'Число вхождений 2 массива в 1 как подпоследовательности: {occurrences}')
