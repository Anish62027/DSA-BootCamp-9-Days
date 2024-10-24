def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

arr = []  
target = None 

while True:
    choice = int(input("""
    Enter a Number:
    1. Enter input
    2. Enter Key
    3. Linear Search
    4. Exit
    """))

    if choice == 1:
        arr = [] 
        for i in range(1, 11):
            a = int(input("Enter an Array element: "))
            arr.append(a)
        print(f"Array: {arr}")

    elif choice == 2:
        target = int(input("Enter Key Value: "))
    
    elif choice == 3:
        if not arr:
            print("array is empty")
        elif target is None:
            print("Target key is not set")
        else:
            result = linear_search(arr, target)
            if result == -1:
                print("Target not found")
            else:
                print(f"Target found at index: {result}")

    elif choice == 4:
        print("Exits the program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 4.")
