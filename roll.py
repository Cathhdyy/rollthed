import random
print("Wlcome to Roll-The-Dice")
print("Discription : The player tp reach 20 score wins the game")
print("Enter 'x' to begin or 'e' to exit")
a=input()
if a=='x' or a=='X':
    print("Enter Player 1 name :")
    p1=input()
    print("Enter Player 2 name :")
    p2=input()
    print("~~~~~~~~~~~")
    print("The game begins you may roll the dice pressing 'r'")
    s1=0
    s2=0
    while s1<=20 and s2<=20:
        print()
        print(p1,"Roll the dice")
        inn=input()
        if inn=='r' or inn=='R':
             ss1=random.randint(1, 6)
             s1+=ss1
             print(ss1,"it is, current score",s1)
        print()
        print(p2,"Roll the dice")
        inn=input()
        if inn=='r' or inn=='R': 
             ss2=random.randint(1, 6)
             s2+=ss2
             print(ss2,"it is, current score",s2)
    if s1>s2:
         print(p1,"is the winner with score",s1)
    else :
         print(p2,"is the winner with score",s2)
