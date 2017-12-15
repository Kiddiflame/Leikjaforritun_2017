from random import *
class Card(object):
    name = ""
    value = 0
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BlackJack():
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.shufle()
        self.run = True
        self.points = 50000
        self.playerHand=[]
        self.houseHand=[]
        self.running()

    def shufle(self):
        newDeck = []
        rng=0
        while(0 < len(self.deck)):
            rng=randint(0,len(self.deck)-1)
            newDeck.append(self.deck[rng])
            del self.deck[rng]
        self.deck=newDeck

    def createDeck(self):
        CardType= ["Clubs","Diamonds", "Hearts", "Spades"]
        for i in range(4):
            for k in range(13):
                if(k == 0):
                    self.deck.append(Card("Ace of "+CardType[i],1))
                elif(k==10):
                    self.deck.append(Card("Jack of " + CardType[i],10))
                elif (k == 11):
                    self.deck.append(Card("Queen of " + CardType[i],10))
                elif (k == 12):
                    self.deck.append(Card("King of " + CardType[i],10))
                else:
                    self.deck.append(Card(str(k+1)+" of " + CardType[i], k+1))

    def running(self):
        options = ["hit me","fold","quit"]
        bet =0
        kek =""#just a filler varuble
        cardIndex = 2
        handSum = 0
        while(self.run==True and self.points > 500 and self.points< 150000):
            bet = 0
            while(bet<500 or bet>self.points):#this will run aslong as you bet the wrong amount
                bet = int(input("how much do you want to bet? "))
                if(bet<500):
                    print("minimal bet is 500")
                elif(bet>self.points):
                    print("you can't bet more then you have")
            self.playerHand.append(self.deck[0])
            self.playerHand.append(self.deck[1])

            for i in range(3):#type out the options
                print(str(i+1)+": "+options[i])

            while(kek != "2" and kek != "3"):#players turn
                handSum = 0
                print("your hand is:")
                for i in range(len(self.playerHand)):
                    print(self.playerHand[i].name+" valued at "+str(self.playerHand[i].value))
                    handSum+=self.playerHand[i].value
                print("totaling up to: "+str(handSum))
                if(handSum>21):
                    print("you're overbooked")
                kek=input("option number: ")
                if kek == "1":
                    self.playerHand.append(self.deck[cardIndex])
                    print(self.deck[cardIndex].name+" was added")
                    cardIndex+=1
            if kek != "3":
                self.houseHand.append(self.deck[cardIndex])
                self.houseHand.append(self.deck[cardIndex + 1])
                cardIndex += 2
                handSum = 0

                while (self.estimit()):  # if there is a more then 50% chance you lose, don't draw
                    print("The house draws a card")
                    self.houseHand.append(cardIndex)
                    cardIndex += 1
                print("the house folds")

                handSum = 0
                for i in range(len(self.houseHand)):
                    print(self.playerHand[i].name)
                    handSum += self.houseHand[i].value
                print("totaling up to: " + handSum)

    def estimit(self):
        sum = 0
        good = 0
        bad = 0
        for k in range(len(self.houseHand)):
            sum += self.houseHand[k].value
        for i in range(52):
            sum = 0
            if(i<len(self.playerHand) or i> len(self.playerHand)+len(self.houseHand)):#if it's not your card
                if self.deck[i].value+sum > 21:
                    bad+=1
                else:
                    good+=1
        if good>bad:
            return True
        else:
            return False



game = BlackJack()