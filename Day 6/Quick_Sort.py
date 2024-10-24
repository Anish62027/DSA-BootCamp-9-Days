def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = []

while True:
    choice = int(input("""
    Menu:
    1. Create a array
    2. quick sort
    3. Exit
    Enter your choice: """))

    if choice == 1:
        arr = []
        n = int(input("Enter the number of elements in the array: "))
        for i in range(n):
            elem = int(input(f"Enter element {i + 1}: "))
            arr.append(elem)
        print(f"Array: {arr}")

    elif choice == 2:
        if not arr:
            print("Array is empty.")
        else:
            sorted_arr = quick_sort(arr)
            print(f"Sorted array: {sorted_arr}")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 3.")

