"""
Jumbled word game : Jumbled word is given to player, player has to rearrange the characters of the word to make
a correct meaningful word.

This is a two players game, firstly program pick a random word from the given list of words using choice()
method of random module. After shuffling the characters of picked word using sample method of random module and
shows the jumbled word on the screen. Current player should give the answer; if it gives the correct answer
after rearranging the characters then player’s score is incremented by one otherwise not.
After quitting the game, winner is decided on the basis of scores.

choice() method randomly choose any word from the list.
sample() method shuffling the characters of the word.
"""
import random


def choose():
    words = ["mathematics", "chemistry", "elephant", "condition", "algorithms", "characters", "rainbow", "handling",
             "microseconds", "temperature", "resource", "networks", "transmission", "connectivity"]
    pick = random.choice(words)
    return pick


def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled


def thank(p1name, p2name, pp1, pp2):
    print("=============================================")
    print("Thanks for playing " + p1name + " and " + p2name+".")
    print(p1name+" your score is "+str(pp1)+".")
    print(p2name+" your score is "+str(pp2)+".")
    if pp1 > pp2:
        print(p1name+" Congratulations! You Win.")
    elif pp1 == pp2:
        print("There is a tie.")
    else:
        print(p2name + " Congratulations! You Win.")


def play():
    p1name = input("Player1, Enter your name: ")  # p1name - player 1 name
    p2name = input("Player2, Enter your name: ")  # p2name - player 2 name
    pp1 = 0  # pp1 - points of player 1
    pp2 = 0  # pp2 - points of player 2
    turn = 0
    while 1:
        # computer's task
        picked_word = choose()
        # create question
        question = jumble(picked_word)
        print(question)

        # player 1
        if turn % 2 == 0:
            print(p1name + ", this is your turn.")
            answer = input("Guess, What is on my mind? ")
            if answer == picked_word:
                pp1 += 1
                print(p1name + " your new score is " + str(pp1) + ".")
            else:
                print("Better luck next time!")
                print("Correct word is " + picked_word + ".")

            c = int(input("Press 1 to continue and 0 to quit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break

        # player 2
        else:
            print(p2name + ", this is your turn.")
            answer = input("Guess, What is on my mind? ")
            if answer == picked_word:
                pp2 += 1
                print(p2name + " your new score is " + str(pp2) + ".")
            else:
                print("Better luck next time!")
                print("Correct word is " + picked_word + ".")

            c = int(input("Press 1 to continue and 0 to quit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break

        # increment turn by 1
        turn += 1


play()
