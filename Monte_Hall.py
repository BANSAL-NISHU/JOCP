"""
Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others,
goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which
has a goat. He then says to you,
“Do you want to pick door No. 2?” Is it to your advantage to switch your choice?
"""
import random

print("Welcome to the Monte Hall problem!")
print("You have the choice of three doors 0, 1, and 2.")

doors = [0]*3
goatdoor = [0]*2
swap = 0          # number of wins with swap
not_swap = 0      # number of wins without swap

# this randomly generated door x (from numbers 1, 2, and 3) will contain the BMW (the prize)
x = random.randint(0, 2)
doors[x] = "BMW"

for i in range(3):
    if i == x:
        continue
    else:
        doors[i] = "Goat"
        goatdoor.append(i)

choice = int(input("Enter your choice: "))

# we only want to open the door which has the goat behind it. So, consider goatdoor only
door_open = random.choice(goatdoor)

while door_open == choice:    # door_open should not be equal to the choice of the user
    door_open = random.choice(goatdoor)

print("************")
print("Door open having goat:", door_open)
decision = input("Do you want to swap? (y/n): ")
if decision == "y":
    if doors[choice] == "Goat":
        print("You Win")
        swap += 1
    else:
        print("You lose")

else:
    if doors[choice] == "Goat":
        print("You lose")
    else:
        print("You win")
        not_swap += 1

print("Number of wins with swap:", swap)
print("Number of wins with not swap:", not_swap)

