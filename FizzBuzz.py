"""
Any number divisible by three is replaced by the word Fizz.
Any number divisible by five is replaced by the word Buzz.
Numbers divisible by 3 and 5 both (or 15) become FizzBuzz.

"""

r = int(input("Enter the maximum range: "))

for i in range(1, r):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        if i % 5 == 0:
            print("Buzz")
        else:
            if i % 3 == 0:
                print("Fizz")
            else:
                print(i)
