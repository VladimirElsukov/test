def is_subarray_equal(arr1, arr2, i):

    return arr1[i:i + len(arr2)] == arr2

def count_subarray_occurrences(arr1, arr2):
    count = 0

    for i in range(len(arr1) - len(arr2) + 1):
        if is_subarray_equal(arr1, arr2, i):
            count += 1
    return count


