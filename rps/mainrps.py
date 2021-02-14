#A simple little game using Python
#Using the random library
#v 1.0: added main game functions, basic gameplay
#v 2.0: Will add play again option. Also added runtime(total time spent playing the game).
from timeit import default_timer as timer
import random
start = timer()
#importing random for random.choice()
def play_rps():
    import random
    # Notifying user with the credits and stuff
    print("Hello, and welcome to RockPaperScissors, credits to @abhishekshahane, v2.0")
    print("You are currently using v2.0. No further updates planned as of now.")
    print("v1.0->v2.0")
    print("Use 'git pull' to update your version of RockPaperScissors to v2.0")
    # List, input and random.choice(list)
    list = ["Rock","Paper", "Scissors"]
    a=input("Enter a option(First letter in caps):  ")
    b = random.choice(list)
    #Making function errorchecking
    if (a not in list):
        def errorchecking(a):

            print("Please enter a valid value.")
            print("If you want to play again, run python rps.py")
            exit()
        errorchecking(a)

    # Making main game function
    elif (a in list):
        def rpsmain(a,b):
            score = 0
            
            
            b = random.choice(list)
            if b=="Scissors" and a=="Paper":
                print("Computer won, now exiting")
                print(f"Computer chose {b}")
                score-=1
            elif b=="Paper" and a=="Rock":
                print("Computer won, now exiting")
                print(f"Computer chose {b}")
                score-=1
            elif b=="Rock" and a=="Scissors":
                print("Computer won, now exiting")
                print(f"Computer chose {b}")
                score-=1
            elif a=="Scissors" and b=="Paper":
                print("You won, now exiting")
                print(f"Computer chose {b}")
                score+=1
            elif a=="Paper" and b=="Rock":
                print("You won, now exiting")
                print(f"Computer chose {b}")
                score+=1
            elif a=="Rock" and b=="Scissors":
                print("You won, now exiting")
                print(f"Computer chose {b}")
                score+=1
            elif a==b:
                print("Tie")
                print(f"Computer chose {b}")
                score+=0
            playA = input("Do you want to play again (y/n) ?").lower()
            if playA == "y":
                play_rps()
            else:
                end = timer()
                x = input("Enter your name: ")
                print(f"Your score is {score}")
                print(f"{x} spent {str((end - start))[:3]} seconds playing this game, now exiting.")
                exit()

        rpsmain(a,b)

play_rps()
# Calling them at the end of this process
