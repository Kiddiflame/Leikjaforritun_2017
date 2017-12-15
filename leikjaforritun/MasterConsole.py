from random import *
class MasterConsole():
    def __init__(self):
        self.running()
    CC = 0
    CV = 0
    playing = True
    preSelectedAnswer = []
    symbols = ["y","r","g","b","w","p","o"]

    def initialize(self):
        CC = 0
        CV = 0
        names = ["yellow","red","green","blue","white","purple","orange"]
        self.preSelectedAnswer = [self.symbols[randint(0,6)],self.symbols[randint(0,6)],self.symbols[randint(0,6)],self.symbols[randint(0,6)]]
        for i in range(7):
            print( self.symbols[i]+": "+names[i])

    def running(self):
        run = True
        guesses = 0
        guess = []
        reply = ""
        while(run == True):
            self.initialize()
            guesses = 0
            while guesses<12 and guess != self.preSelectedAnswer:
                guess = (list(map(str, input('guess (sample input is four letters split with commas, like so: y,r,g,b) :').split(','))))
                print(self.check(guess))
            if(guess == self.preSelectedAnswer):
                print ("you won")
            else:
                print ("you lost")
            reply = input("would you like to play again ('y') for yes")
            if reply == "y":
                run = True
            else:
                run = False

    def check(self, listinn):
        done = []
        bul = True
        self.CC=0
        self.CV=0
        for i in range(7):
            if(self.symbols[i] in self.preSelectedAnswer and self.symbols[i] in listinn):#check if they both have the symbol
                a = 0#counters
                b = 0
                for k in range(4):
                    if self.preSelectedAnswer[k]==listinn[k] and self.symbols[i] == listinn[k] and self.symbols[i] == self.preSelectedAnswer[k]:
                        self.CC+=1
                    else:
                        if (self.symbols[i] == self.preSelectedAnswer[k]):
                            a += 1
                        if (self.symbols[i] == listinn[k]):
                            b += 1
                self.CV+=min(a,b)
        return "there are "+str(self.CC)+" colors on the correct place and correct place, and there are "+str(self.CV)+" colors correct but in the incorrect place"

classinn = MasterConsole()