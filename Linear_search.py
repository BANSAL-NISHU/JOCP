def linear_search(n, x):
    element = []
    for i in range(1, n+1):
        element.append(i)

    count = 0  # counting the number of iteration
    flag = 0
    for i in element:
        count += 1
        if i == x:
            print("Number found at position "+str(i)+".")
            flag = 1
            break

    if flag == 0:
        print("Number is not found.")

    print("Number of iterations: "+str(count))


linear_search(1000, 1000)
