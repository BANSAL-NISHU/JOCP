"""
The Fibonacci series is a series of numbers where a number is the addition of the last two numbers,
starting with 0, and 1.
The Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, .....

Written as a rule, the expression is:
Xn = Xn-1 + Xn-2
"""

print("Program to print n terms of fibonacci series.")
n = int(input("Enter the value of n: "))
a = -1
b = 1

for i in range(1,n+1):
    c = a+b
    print(c,end=" ")
    a = b
    b = c

print("\nThese are first "+str(n)+" terms of fibonacci series.")