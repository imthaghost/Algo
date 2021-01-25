# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the first one.
def isValidSubsequence(array, sequence):
    for i in range(len(sequence) -1):
        p1 = sequence[i]
        if p1 in array:
            p1 = sequence[i] + 1
        else:
            return false
    return true        
