import math

def jump_search(array, x, n):
    """Write your code here."""
    def linear_search(arr):
        for item in arr:
            if item == x:
                return array.index(item)
        return -1
            
    step = int(math.sqrt(n))
    i = 0
    while i <= n and len(array[i:]) >= step:
        if array[i+step-1] == x:
            return i+step-1
        elif array[i+step-1] > x:
            return linear_search(array[i:i+step-1])
        i += step
    return linear_search(array[i:])


if __name__ == '__main__':

    int_arr = list(map(int, input().split(' ')))
    target = int(input())
    
    # Function call
    result = jump_search(int_arr, target, len(int_arr) - 1)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")