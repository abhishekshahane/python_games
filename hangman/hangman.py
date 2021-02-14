from getpass import getpass
#WARNING: ONE WORD ONLY, will add multiple words in a later update maybe
#lol this is just to check my python skills on classes 
class Hangman:
    def __init__(self,input1):
        self.input1 = input1
    def play(self):
        def remove(a,li):
            return [val for val in li if val!=a]
        def check_win(li, input1):
            return ''.join(li)==input1
        if len(self.input1.split())>1:
            print("Sorry, but multiple words aren't supported at this time!")
        else:
            li = [letter for letter in self.input1]
            lia = ['_' for letter in self.input1]
            for each in lia:
                print(each,end=" ")
            print()
            for j in range(len(self.input1)):
                print(j+1, end=" ")
            print()
            count = 7
            #main game loop
            while count!=0:
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
                    print("Sorry, letter doesn't fit!")
                    count-=1
            if count==0:
                print("Sorry, you lost")
            else:
                print("Nice, you got the word")

input1 = getpass()
c = Hangman(input1)
c.play()
