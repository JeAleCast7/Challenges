import random
judge = ""

print("Let's play rock, paper, scissors")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
while True:
    game = int(input("Enter your game: \n"))
    if game == 1:
        game = "Rock"
        break
    elif game == 2:
        game = "Paper"
        break
    elif game == 3:
        game = "Scissors"
        break
    else:
        print("Invalid")
    
mix = random.randint(1, 3)

if mix == 1:
    mix = "Rock"
elif mix == 2:
    mix = "Paper"
elif mix == 3:
    mix = "Scissors"

if game == mix:
    judge = "DRAW"
elif (game == "Rock" and mix == "Scissors") or (game == "Scissors" and mix == "Rock"):
    judge = "Rock wins"
elif (game == "Paper" and mix == "Rock") or (game == "Rock" and mix == "Paper"):
    judge = "Paper wins"
elif (game == "Scissors" and mix == "Paper") or (game == "Paper" and mix == "Scissors"):
    judge = "Scissors win"
    
print("your game: ", game, " vs ", mix)
print("Who won? : ", judge)