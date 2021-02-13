"""
Highest Common Factor (HCF) or Greatest Common Divisor (GCD) is the greatest factor which is common to any two
given numbers.

Applications:
1. To split things into smaller sections.
2. To equally distribute any number of sets of items into their largest grouping.
3. To figure out how many people we can invite.
4. To arrange something into rows or groups.

"""

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

x = min(m,n)     #smallest number between two given numbers

for i in range(1,x+1):
    if m%i==0 and n%i==0:
        hcf = i

print("HCF of " + str(m) + " and " + str(n) + " is " + str(hcf) + ".")
