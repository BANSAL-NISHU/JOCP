def rock_paper_scissors(num1, num2, bit1, bit2):
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3
    if player_one[p1] == player_two[p2]:
        print("Draw")

    elif player_one[p1] == "Rock" and player_two[p2] == "Scissor":
        print("Player1 Wins!")
    elif player_one[p1] == "Rock" and player_two[p2] == "Paper":
        print("Player2 Wins!")

    elif player_one[p1] == "Paper" and player_two[p2] == "Scissor":
        print("Player2 Wins!")
    elif player_one[p1] == "Paper" and player_two[p2] == "Rock":
        print("Player1 Wins!")

    elif player_one[p1] == "Scissor" and player_two[p2] == "Paper":
        print("Player1 Wins!")
    elif player_one[p1] == "Scissor" and player_two[p2] == "Rock":
        print("Player2 Wins!")


player_one = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
player_two = {0: 'Paper', 1: 'Rock', 2: 'Scissor'}
while 1:
    num1 = input("Player1, Enter your choice: ")  # choice of player 1
    num2 = input("Player2, Enter your choice: ")  # choice of player 2
    bit1 = int(input("Player1, Enter the secret bit position: "))
    bit2 = int(input("Player2, Enter the secret bit position: "))

    rock_paper_scissors(num1, num2, bit1, bit2)

    choice = input("Do you want to continue? (y/n): ")
    if choice == 'n':
        break
