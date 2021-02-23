def binary_search(arr, x):
    first_position = 0
    last_position = len(arr) - 1
    flag = 0  # flag 0 means that the element has not been found yet
    count = 0

    while first_position <= last_position and flag == 0:
        count += 1
        mid = (first_position + last_position) // 2
        if x == arr[mid]:
            flag = 1
            print("Number is found at position: "+str(mid))
            print("Number of iterations: "+str(count))
            return
        else:
            if x < arr[mid]:
                last_position = mid - 1
            else:
                first_position = mid + 1

    print("The number is not found.")


arr = []
for i in range(501):
    arr.append(i)

binary_search(arr, 96)
