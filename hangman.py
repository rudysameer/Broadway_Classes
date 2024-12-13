import random

def hangman():
    word = ["Deepika","Anuskha","Kareena","Katrina","Shruti Hasan","Illiana","Tripti","Kiara","Alia","Brooke Shields","Lana Rhodes","Mia Melano","Sumnima"]
    choice = random.choice(word)
    validchoices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    turns = 10
    guessmade = ''

    while len(choice)>0:
        main = ""
        missed = 0

        for letter in choice:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_"+" "

        if main == choice:
            print(main)
            print("You are Saved. Congrats")        
            break  

        if turns == 0:
            print("kind man died")
            print("Answer was ",choice)
            break         

        print(turns," guesses left")
        print("guess the word ",main)
        guess = input()
            

        if guess in validchoices:
            guessmade = guessmade + guess
        else:
            print("enter a valid characters")
            guess = input()
        if guess not in choice:
            turns = turns -1  
            if(turns == 9):
                print("___________")
            if(turns == 8):
                print("___________")
                print("     O     ")
            if(turns == 7):
                print("___________")
                print("     O     ")
                print("     |    ")
            if(turns == 6):
                print("___________")
                print("     _O     ")
                print("      |    ")
            if(turns == 5):
                print("___________")
                print("     _O_     ")
                print("      |    ")
            if(turns == 4):
                print("___________")
                print("     _O_     ")
                print("      |    ")
                print("     /     ")
            if(turns == 3):
                print("___________")
                print("     _O_     ")
                print("      |    ")
                print("     / \    ")
            if(turns == 2):
                print("___________")
                print("     _O_   |  ")
                print("      |    |")
                print("     / \   |")
            if(turns == 1):
                print("____|__|_____")
                print("     _O_   |  ")
                print("      |    |")
                print("     / \   |")


            if(turns == 0):
                print("Rest in Peace")
                print("_____|_|___")
                print("     |O|   |  ")
                print("     /|\   |")
                print("     / \   |")



               







name = input("Enter Your Name\n")
print("Welcome to the HAngman Organization. ",name,"'s Life is in Danger")
print("_________________")
print(name,"'s Life is in your Guesses. Guess the word in 10 chnaces")

hangman()
   
