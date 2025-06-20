def bubble_sort(unsorted_list):

    n = len(unsorted_list)

    for i in range(n): 
        swapped = False
        for j in range(0, n - i - 1): 
            if unsorted_list[j] > unsorted_list[j + 1]: # swap if the element found is greater then the next element
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # if no two elements were swapped by inner loop, then break, because the list is alread sorted
        if not swapped:
            break
    return unsorted_list
