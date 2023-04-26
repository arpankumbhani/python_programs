#make a two player rock-paper-seissor game.
player1=input("player 1:")
player2=input("player 2")
if player1=="rock"and player2=="paper":
    print("player 2 is winner")
elif player1=="rock"and player2=="scissor":
    print("player 1 is winner")
elif player1=="paper"and player2=="scissor":
    print("player 2 is winner")
elif player1=="paper"and player2=="rock":
    print("player 1 is winner")
elif player1=="scissor"and player2=="paper":
    print("player 2 is winner")
elif player1=="scissor"and player2=="rock":
    print("player 2 is winner")
elif player1==player2:
    print("it is tie")
