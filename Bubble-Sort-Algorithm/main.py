# Bubble Sort Algorithm implementation in python
arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]


def bubble_sort(sequence):
    n = len(sequence)
    # loop to access each array sequence
    for i in range(n - 1):
        # loop to compare array sequence
        for j in range(n - 1 - i):
            # Adjacent sequence element comparison
            # sort > to < to sort in descending order
            if sequence[j] > sequence[j + 1]:
                # swapping sequence if elements are not in the intended order
                temp = sequence[j]
                sequence[j] = sequence[j + 1]
                sequence[j + 1] = temp
    return sequence


print(bubble_sort(arr))
