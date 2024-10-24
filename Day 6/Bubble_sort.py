def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = []

while True:
    choice = int(input("""
    Menu:
    1. Create a array
    2. bubble sort
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
            sorted_arr = bubble_sort(arr)
            print(f"Sorted array: {sorted_arr}")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 3.")


