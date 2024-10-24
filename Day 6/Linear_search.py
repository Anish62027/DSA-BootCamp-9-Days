def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(arr, target)
print(f"Linear Search: Target {target} found at index {result}" if result != -1 else "Target not found")
