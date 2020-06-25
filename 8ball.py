import random
print("Magic8ball, v1.0")
choices = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
randomchoice = random.choice(choices)
a = input("Enter your name:  ")
def main(randomchoice):
    b = input("Enter your question: ")
    print(f"Answer for {b}: {randomchoice}")
    playagain(a)
    
def playagain(a):
    f = input("Do you want to play again(yes/no):    ")
    if(f == "yes"):
        print(f"C'mon {a}, Let's play it again!")
        main(randomchoice)
    elif(f == "no"):
        print(f"Oh..Come back to play next time, {a}!")
        exit()
    else:
        print(f"Sorry {a}, didn't quite catch that. Let's try again.")
        playagain(a)
main(randomchoice)
