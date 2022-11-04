def bubble_sort(L):
    """Sort a list of elements using bubble sort algorithm"""
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


def selection_sort(L):
    """Sort a list of elements using selection sort algorithm"""
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L


def insertion_sort(L):
    """Sort a list of elements using insertion sort algorithm"""
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
    return L


def merge_sort(L):
    """Sort a list of elements using merge sort algorithm"""
    if len(L) < 2:
        return L
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    """Merge two sorted lists"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def quicksort(L):
    """Sort a list of elements using quicksort algorithm"""
    if len(L) < 2:
        return L
    else:
        pivot = L[0]
        less = [i for i in L[1:] if i <= pivot]
        greater = [i for i in L[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    import timeit
    from random import shuffle

    for sort in [bubble_sort, selection_sort, insertion_sort, merge_sort,
                 quicksort]:
        L = list(range(1000))
        shuffle(L)
        t = timeit.Timer('sort(L)', 'from __main__ import sort, L')
        print('Time for {}: {}'.format(sort.__name__, t.timeit(number=1)))
