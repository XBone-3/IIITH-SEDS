# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binary_search(arr, l, h, target):
    if (l >= h):
        if (target == arr[l]):
            return l
        else:
            return -1
    else:
        mid = (l + h) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, l, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, h, target)

if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    n = len(int_arr)
    target = int(input())
    
    # Function call
    result = binary_search(int_arr, 0, len(int_arr) - 1, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")