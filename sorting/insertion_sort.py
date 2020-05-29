def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) or O(n*(n-1)) for each item we have to compare to every other item in the array minus the previous ammount hence n-1 
    Memory usage: O(1) We do not allocate any more memory than that was already given"""

    length = len(items)
    # Traverse through 1 to length
    for i in range(1, length):
        # key is the current value
        key = items[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
    
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key