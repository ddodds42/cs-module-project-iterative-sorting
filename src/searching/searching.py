def linear_search(arr, target):
    # if current == target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    # report the index
    # else, next index val

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # sort the array
    rclaw = arr.sort()
    # mark head and tail
    head = 0
    tail = len(arr) - 1

    # until head and tail not meet
    while tail >= head:
        # locate median
        median = (head + tail) // 2
        # is median the target?
        if arr[median] == target:
            # return median
            return median
        # if median less than target
        else:
            if target > arr[median]:
                # shift head
                head = median + 1
            # if median greater than target
            if target < arr[median]:
                # shift tail
                tail = median - 1

    return -1  # not found
