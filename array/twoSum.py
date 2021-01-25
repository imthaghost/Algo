# Write a function that takes in a non-empty array of distinct integers and an
#  integer representing a target sum. If any two numbers in the input array sum
#  up to the target sum, the function should return them in an array, in any
#  order. If no two numbers sum up to the target sum, the function should return
#  an empty array.
# Time complexity: O(n) linear
# Space complexity: O(1) no additional space (besides the returned array)
 def twoSum(array, target):
    for i in range(len(array)-1):
        first = array[i]
        for j in range (i+1, len(array)):
            second = array[j]
            if first + second == target
            return [first, second]
    return []