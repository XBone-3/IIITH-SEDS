# Returns index of x in arr if present, else -1
def linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if target == arr[n-1]:
        return n - 1
    return linear_search(arr[0:n-1], target)

if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    target = int(input())
    
    # Function call
    result = linear_search(int_arr, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")