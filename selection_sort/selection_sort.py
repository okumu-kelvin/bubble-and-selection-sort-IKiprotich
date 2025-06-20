def selection_sort(unsorted_list):

    n = len(unsorted_list)

    for i in range(n):
        # assume the minimum is the first element
        min_index = i
        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        # swap the found minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
        
    return unsorted_list
