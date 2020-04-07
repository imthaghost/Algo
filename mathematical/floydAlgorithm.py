
"""
Find Duplicate Number

Given an array nums containing n + 1 integers where each integer is 
between 1 an n prove that one duplicate number must exist

"""

"""
Time Complexity: O(n)
Space Complexity: O(1)

Description: The algorithm thus maintains two pointers into the given sequence, 
one (slow) at xi, and the other (fast) at x2i. 
At each step of the algorithm, it increases i by one, 
moving slow one step forward and fast two steps 
forward in the sequence, and then compares the sequence values 
at these two pointers. The smallest value of i > 0 
for which slow and fast point to 
equal values is the desired value ν

Reference: https://en.wikipedia.org/wiki/Cycle_detection

"""


def findDuplicates(nums):

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    ptr1 = nums[0]
    ptr2 = slow

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


arr = [4, 1, 4, 7, 2]
d = findDuplicates(arr)
print(d)
