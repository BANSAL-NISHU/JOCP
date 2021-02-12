"""
Magic number,M = n(n^2+1)/2
Conditions:
1. In any magic square, 1 is located at position(n/2,n-1).
2. Let's say the position of 1 i.e.(n/2,n-1) is (p,q), then next number which is 2 is located at (p-1,q+1) position.
Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0.
3. If the calculated position already contains a number, then decrement the column by 2 and increment the row by 1.
4. If anytime row position becomes -1 and column becomes n (together), switch it to (0,n-2).

"""


def MagicSquare(n):
    magic_square = []

    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magic_square.append(l)

    i = n // 2                                                # Condition 1
    j = n - 1
    num = n * n
    count = 1

    while (count <= num):
        if (i == -1 and j == n):                              # Condition 4
            i = 0
            j = n - 2
        else:
            if (j == n):        # Column n -> 0
                j = 0

            if (i < 0):         # Row -1 -> n-1
                i = n - 1

        if (magic_square[i][j] != 0):                         # Condition 3
            i = i + 1
            j = j - 2
            continue
        else:
            magic_square[i][j] = count
            count += 1

        i = i - 1                                             # Condition 2
        j = j + 1

    for i in range(n):
        for j in range(n):
            print(magic_square[i][j], end=" ")
        print()

    print("The sum of each row/column/diagonal: " + str(n * (n ** 2 + 1) / 2))
