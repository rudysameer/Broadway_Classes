import random


x = "y"
while x == "y":
    dice = random.randint(1,6)
    print(dice)

    if dice == 1:
        print("______________")
        print("|            |")
        print("|            |")
        print("|      O     |")
        print("|            |")
        print("|____________|")
    if dice == 2:
        print("______________")
        print("|            |")
        print("|            |")
        print("|    O  O    |")
        print("|            |")
        print("|____________|")
    if dice == 4:
        print("______________")
        print("|            |")
        print("|    O  O    |")
        print("|            |")
        print("|    O  O    |")
        print("|____________|")
    if dice == 3:
        print("______________")
        print("|            |")
        print("|            |")
        print("|   O  O  O  |")
        print("|            |")
        print("|____________|")

    if dice == 6:
        print("______________")
        print("|            |")
        print("|    O  O    |")
        print("|    O  O    |")
        print("|    O  O    |")
        print("|____________|")

    if dice == 5:
        print("______________")
        print("|            |")
        print("|    O   O   |")
        print("|      O     |")
        print("|    O   O   |")
        print("|____________|")


    x = input("Wanna roll it again y/n  :")      
    