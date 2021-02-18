import random


def evolve(x):
    index = random.randint(0, len(x)-1)   # since both ends are inclusive
    p = random.randint(1, 100)
    if p == 1:
        if x[index] == '0':
            x[index] = '1'
        else:
            x[index] = '0'


with open("dna_data.txt") as myfile:
    x = myfile.read()
    x = list(x)
    print(len(x))


for i in range(0, 10000):
    evolve(x)

print(x)
