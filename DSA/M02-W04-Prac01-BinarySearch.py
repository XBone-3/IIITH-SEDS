# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binary_search(arr, l, h, target):
    count = 0
    while(l <= h):
        count += 1
        mid = (l + h) // 2
        if (arr[mid] == target):
            print(count)
            return mid
        elif (arr[mid] < target):
            l = mid + 1
        else:
            h = mid -1
    print(count)
    return -1


if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(',')))
    n = len(int_arr)
    target = int(input())
    
    # Function call
    result = binary_search(int_arr, 0, len(int_arr) - 1, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")