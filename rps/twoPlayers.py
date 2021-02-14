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
    user1_input = input("Enter your choice!(Rock/Paper/Scissors), this must be typed exactly as specified:  ")
    user2_input = input("Enter your choice, Player 2!(Rock/Paper/Scissors), this must be typed exactly as specified:  ")
    n = main_game_list.index(user1_input)
    if main_game_list[main_game_list.index(user2_input)] == main_game_list[n-1]:
        print("Oops, User2 has won, they chose {}, and you chose {}.".format(user2_input,user1_input))
    elif main_game_list[main_game_list.index(user2_input)] == main_game_list[n]:
        print("It's a tie! You chose {}, and the computer chose {}.".format(user1_input, user2_input))
    else:
        print("Yay! You won! The User2 chose {} and you chose {}.".format(user2_input,user1_input))
    __play_again__(game_loop_bool)
