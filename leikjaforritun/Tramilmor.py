import random
import time

def displayIntro():
    print("After many a sheep and cow has been murdered, by the dread dragon Drafngast, the town of Blackwater decides it has had enough!")
    print("The hero Tramilmore and his 'ever' confident sidekick, Sullumbull, have been tasked with killing it...but what is but a lowly adventurer to do, against a dragon?")
    print("After wandering the countryside, thanks to your ever loyal sidekick misreading the map and missing the clearly marked cave, you finally find it")
    print("A warning stands in front of the cave: To all those who would interlope, you will find your death a painful one. What will you do?")
    print("")
    print("Enter the cave, or leave?")

def choosePath():
    path = ""
    correctpath = "1"
    while path != "1" and path != "2": # input validation

        path = raw_input("The choice is yours: 1/2 :")

        if path != correctpath:
            print("You go home, and the dragon continues to steal and plunder like the dragon he is. Shaaaaaame")
            print("Game Over")
        elif path == correctpath:
            print("You venture into the cave, like the brave adventurer you are!")
            time.sleep(2)
            print("")
            print(
            "Venturing deep into the unexplored cave, a lone drop of water dripping from the ceiling...the darkness barely broken by your torch...")
            time.sleep(2)
            print("")
            print("You see a junction, a wide open room, with 6 doors to choose from")
            print("The door directly in front of you has a big, fiery symbol on it, that says: 'my room' on it. It has a lock that won't open until you solve the riddles in the other 5 rooms")

def firstRoom():
    choices = ""
    print("Opening the first door, you see a wall with two levers, and an unearthly voice speaks aloud in your ear")
    time.sleep(1)
    print("You can anger men, beasts and even gods if you're daring, but what can you anger, that you will never survive?")
    print("")
    while choices != "1" and choices != "2" and choices != "3":
        raw_input("Choices: 1-A demon 2-A Kraken? 3-Your mother?")
        if choices == "1":
            print("There is no reaction, try again")
        elif choices == "2":
            print("Nothing happens, try again")
        else:
            print("The voice speaks again: 'You're damn right'")

def secondRoom():
    choices = ""
    print("Opening the first door, you see a wall with two levers, and an unearthly voice speaks aloud in your ear")
    time.sleep(1)
    print(
    "You can anger men, beasts and even gods if you're daring, but what can you anger, that you will never survive?")
    print("")
    while choices != "1" and choices != "2" and choices != "3":
        raw_input("Choices: 1:A demon 2:A Kraken? 3:Your mother?" )
        if choices == "1":
            print("There is no reaction, try again")
        elif choices == "2":
            print("Nothing happens, try again")
        elif choices == "3":
            choices = ""
            print("'You're damn right'")
            coreRoom()

def coreRoom():
    room1 = None
    room2 = None
    room3 = None
    room4 = None
    room5 = None
    path = ""
    while path != "1" and path != "2" and path != "3" and path != "4" and path != "5":

        path = raw_input("Which path will you choose? 1/5 :")
        if path == "1":
            if room1:
                print("You have already completed this room")
                path = ""
                coreRoom()
            else:
                firstRoom()
            room1 = True

        elif path == "2":
            print("test 2")
            room2 = True

        elif path == "3":
            print("test 3")
            room3 = True

        elif path == "4":
            print("test 4")
            room4 = True

        elif path == "5":
            print("test 5")
            room5 = True




displayIntro()
choosePath()
coreRoom()
