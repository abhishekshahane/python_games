#Isn't as long and without all those annoying if statements
from random import choice
from time import sleep
#The __play_again__ function
def __play_again__(game_loop_bool):
    get_input = input("Do you want to play again(Y/N): ")
    if get_input == "N":
        game_loop_bool = False
        print("Thanks for playing, play next time!")
        sleep(2)
        return game_loop_bool
    else:
        game_loop_bool = True
        return game_loop_bool
game_loop_bool = True
#The main game loop
while game_loop_bool==True:
    main_game_list = ["Paper","Rock","Scissors"]
    users_input = input("Enter your choice!(Rock/Paper/Scissors), this must be typed exactly as specified:  ")
    comps_choice = choice(main_game_list)
    comps_number = main_game_list.index(comps_choice)
    n = main_game_list.index(users_input)
    if main_game_list[comps_number] == main_game_list[n-1]:
        print(f"Oops, the computer has won, they chose {comps_choice}, and you chose {users_input}.")
    elif main_game_list[comps_number] == main_game_list[n]:
        print(f"It's a tie! You chose {users_input}, and the computer chose {comps_choice}.")
    else:
        print(f"Yay! You won! The computer chose {comps_choice} and you chose {users_input}.")
    __play_again__(game_loop_bool)
