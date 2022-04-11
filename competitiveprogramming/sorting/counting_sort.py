def counting_sort(array):
    """The lower bound Ω(n log n) does not apply to algorithms
    that do not compare array elements but use some other
    information. Can only be used when the constant c is small enough,
    so that the array elements can be used as indices
    in the bookkeeping array.
    Best case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)
    Average case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)
    Worst case running time: O(n^c) if c is a very large integer
    that is not within the range of 0-c such that c ≠ O(n)
    Memory usage: O(1) We use a partial hashing algorithm to count
    the occurrence of the data.  """

    size = len(array)

    # The output integer array that will have the sorted array
    output = [0] * size

    # Hash array
    count = [0] * 10

    # Create a count array to store count of individual
    # integers and initialize count array as 0
    for i in range(size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]

items = [0, 4, 1, 3,5,9]
counting_sort(items)
print(items)