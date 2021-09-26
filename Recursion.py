# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# n = int(input("Enter a positive number: "))
# print("Factorial of", n, "is", factorial(n))


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        print("fibonacci(n-1) when n=", n, "is", fibonacci(n-1))
        print("fibonacci(n-2) when n=", n, "is", fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(4))