import random

print("Let's play rock, paper, scissors")
print("1) Rock")
print("2) Paper")
print("3) Scissors")

game = int(input("Enter your game: \n"))

if game == 1:
    game = "Rock"
elif game == 2:
    game = "Paper"
elif game == 3:
    game = "Scissors"
else:
    print("Invalid")
    
mix = random.randint(1, 3)

if mix == 1:
    mix = "Rock"
elif mix == 2:
    mix = "Paper"
elif mix == 3:
    mix = "Scissors"

if game == "Rock" and mix == "Rock":
    judge = "DRAW"
elif game == "Paper" and mix == "Paper":
    judge = "DRAW"
elif game == "Scissors" and mix == "Scissors":
    judge = "DRAW"
elif game == "Rock" and mix == "Scissors":
    judge = "Rock wins"
elif game == "Paper" and mix == "Rock":
    judge = "Paper wins"
elif game == "Scissors" and mix == "Paper":
    judge = "Scissors win"
    
print("your game: ", game, " vs Machine: ", mix)
print("Who won? : ", judge)