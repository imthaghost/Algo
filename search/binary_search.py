
def binary_search_recursive(array, target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    # return the index
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_search_recursive(array, target, left, mid -1)
    else: 
        return binary_search_recursive(array, target, mid+1, right)

def binary_search_iterative(array, target):
    left = 0
    right = len(array) - 1 
    mid = 0
    
    while left <= right:

        mid = (left + right) // 2
        # if target is greater than mid value ignore left half
        if target > arr[mid]:
            left = mid + 1
        # if target is less than mid value ignore right half
        elif target < arr[mid]:
            right = mid - 1
        # if target is equal to mid value return
        else:
            return mid


arr = [1,2,3,4,5,6]
print(binary_search_recursive(arr, 0, 0, len(arr)-1))
print(binary_search_iterative(arr, 2))