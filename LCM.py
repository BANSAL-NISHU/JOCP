"""
Lowest Common Multiple (LCM) is the smallest number (other than zero) that is the common multiple of any
two given numbers.

Applications:
1. About an event that is or will be repeating over and over.
2. To purchase or get multiple items in order to have enough.
3. To analyse when something will happen again at the same time.

"""

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

x = max(m, n)                     #largest number between two given numbers

for i in range(x, (m * n) + 1, x):
    if i % m == 0 and i % n == 0:
        break

print("LCM of " + str(m) + " and " + str(n) + " is " + str(i) + ".")