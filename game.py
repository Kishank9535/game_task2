import random 
options=("Rock","Paper","Scissors")
running=True

while running:
    player=None

    computer=random.choice(options)
    while player not in options:
        player=input("Enter the choice (Rock,Paper,Scissors)\n")
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if player==computer:
        print("!!It's a tie!!")
    elif player=="Rock" and computer=="Scissors":
        print("** You win **")
    elif player=="Paper" and computer=="Rock":
        print("** You win **")
    elif player=="Scissors" and computer=="Paper":
        print("** You win **") 
    else:
        print("You Lose !!") 
    play_again=input("Want to Play again !! (y/n):\n").lower()
    if not play_again=="y" :
           running = False

print("**Thanks for playnig**")             
