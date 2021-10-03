# This is a sample Python script.
import random
print("Hey! This is a Rock-Paper-Scissors Game between you and Player2")
print("Enter your name")
name = input()
print("Rules : s for Stone || p for Paper || sc for Scissors")
q = ("s","p","sc")
p=0
antip=0
while p<=5 and antip<=5:
    print("Play")
    print("Your move ?")
    move = input()
    i = random.choice(q)
    if i == 's':
        if move == 's':
            print("Player2 : Stone ")
            print("You : Stone ")
            print("No points play again")
            print("You:", p, "Player2:", antip)
        if move == 'p':
            print("Player2 : Stone ")
            print("You : Paper ")
            print("Player2 wins this point")
            print("This point goes to you")
            p += 1
            print("You:", p, "Player2:", antip)
        if move == 'sc':
            print("Player2 : Stone ")
            print("You : Scissors ")
            antip += 1
            print("You:", p, "Player2:", antip)
    elif i == 'p':
        if move == 's':
            print("Player2 : Paper ")
            print("You : Stone ")
            print("Player2 wins this point")
            antip += 1
            print("You:", p, "Player2:", antip)
        if move == 'p':
            print("Player2 : Paper ")
            print("You : Paper ")
            print("No points play again")
            print("You:", p, "Player2:", antip)
        if move == 'sc':
            print("Player2 : Paper ")
            print("You : Scissors ")
            print("This point goes to you")
            p += 1
            print("You:",p,"Player2:",antip)
    elif i == 'sc':
        if move == 's':
            print("Player2 : Scissors ")
            print("You : Stone ")
            print("This point goes to you")
            p += 1
            print("You:", p, "Player2:", antip)
        if move == 'p':
            print("Player2 : Scissors ")
            print("You : Paper ")
            print("Player2 wins this point")
            antip += 1
            print("You:", p, "Player2:", antip)
        if move == 'sc':
            print("Player2 : Scissors ")
            print("You : Scissors ")
            print("No points play again")
            print("You:", p, "Player2:", antip)
if p == 4:
    print(name,"won the match")
else:
    print("Player2 won the match")
end =input("Now press 1 to exit")

