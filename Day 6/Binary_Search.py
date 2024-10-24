def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = []
target = None

while True:
    choice = int(input("""
        Menu:
    1. Create array
    2. Enter a target value
    3. Binary search
    4. Exit
    Enter your choice: """))

    if choice == 1:
        arr = []
        n = int(input("Enter the number of elements: "))
        for i in range(n):
            elem = int(input(f"Enter element {i + 1}: "))
            arr.append(elem)
        arr.sort()
        print(f"Array: {arr}")

    elif choice == 2:
        target = int(input("Enter the target value: "))
        print(f"Target set to {target}")

    elif choice == 3:
        if not arr:
            print("Array is empty.")
        else:
            result = binary_search(arr, target)
            if result != -1:
                print(f"Binary Search: Target {target} found at index {result}")
            else:
                print("Target not found")

    elif choice == 4:
        print("Exits the program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 4.")
