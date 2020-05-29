def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    
def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: n*n/2 --> O(n^2) for each item we are checking if the previous is also sorted making the 
    algorithm exponentially propotional to the input size
    Memory usage: O(1) We are modifying the original array not making a copy so 
          the algorithm takes up no additional space than that was already allocated"""

    sorted = False  # is the array sorted
    last = len(items) - 1  # last item sorted is always at the end
    # dont break until the array is sorted
    while not sorted:
        sorted = True
        # for each item in the array
        for i in range(last):
            # bitwise calculation
            # greater()
            if items[i] > items[i+1]:
                # swap values
                swap(items, i, i+1)
                sorted = False
        # decrement is sorted by last value or left value
        last -= 1
    return items