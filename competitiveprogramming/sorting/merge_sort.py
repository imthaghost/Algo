def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlogn + mlogm) n and m are the lengths of th split arrays 
    Memory usage: O(n + m) We create an array of size n + m to fit the contents
    of both arrays inside. The space we need for this operation is linearly
    porportional to both our arrays. """

    # base case and only case
    if len(items) > 1:

        # split the array down the middle
        m = split(items)

        # arrays left half
        lh = items[:m]

        # arrays right half
        rh = items[m:]

        # recursivley call merge_sort() on other halfs
        merge_sort(lh)
        merge_sort(rh)

        # reassign all values
        items[:] = merge(lh, rh)

# helper functions
def split(arr):
    """Return the midpoint of an array"""

    l = len(arr)

    mid = (l // 2)

    return mid

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) n and m are the lengths of both arrays we at least
    have to cycle through both arrays at least once.
    Memory usage: O(n + m) We create an array of size n + m to fit the contents
    of both arrays inside. The space we need for this operation is linearly
    porportional to both our arrays. """

    size1 = len(items1)
    size2 = len(items2)
    items3 = [None] * (size1 + size2)
    i = 0
    j = 0
    k = 0

    # Traverse both arrays
    while i < size1 and j < size2:

        if items1[i] < items2[j]:
            items3[k] = items1[i]
            k = k + 1
            i = i + 1
        else:
            items3[k] = items2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < size1:
        items3[k] = items1[i]
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < size2:
        items3[k] = items2[j]
        k = k + 1
        j = j + 1

    return items3




items = [0, 4, 1, 3,5,9]
merge_sort(items)
print(items)