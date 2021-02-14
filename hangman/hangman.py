from getpass import getpass
#WARNING: ONE WORD ONLY, will add multiple words in a later update maybe
#lol this is just to check my python skills on classes 
class Hangman:
    def __init__(self,input1,asciihangman):
        self.input1 = input1
        self.asciihangman = asciihangman
    def play(self):
        def remove(a,li):
            return [val for val in li if val!=a]
        def check_win(li, input1):
            return ''.join(li)==input1
        if len(self.input1.split())>1:
            print("Sorry, but we do not support multiple words yet!")
        else:
            li = [letter for letter in self.input1]
            lia = ['_' for letter in self.input1]
            for each in lia:
                print(each,end=" ")
            print()
            for j in range(len(self.input1)):
                print(j+1, end=" ")
            print()
            count = 0
            #main game loop
            while count!=7:
                st = ""
                a = input("Enter your one letter guess: ")
                if a in li:
                    li = remove(a,li)
                    for i in range(len(self.input1)):
                        if self.input1[i] not in li:
                            lia[i] = self.input1[i]
                    for z in range(len(lia)):
                        print(lia[z],end=" ")
                    print()
                    for j in range(len(self.input1)):
                        print((j+1), end=" ")
                    print()
                    if check_win(lia,self.input1)==True:
                        break
                else:
                    print(self.asciihangman[count])
                    count+=1
            if count==7:
                print("Sorry, you lost")
            else:
                print("Nice, you got the word")
asciihangman = HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
input1 = getpass()
c = Hangman(input1,asciihangman)
c.play()
