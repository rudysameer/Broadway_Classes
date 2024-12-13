import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    if word in data:
        return (data[word])
    elif word.title() in data:
        return (data[word.title()])
    elif word.upper() in data:
        return (data[word.upper()])
    elif len(get_close_matches(word, data.keys())) >0:
        print("did you mean by %s"%get_close_matches(word, data.keys())[0])
        decide  = input("y for yes n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return("not availabele")

    else:
        print("sorry word doesnot exist in the dictionary")


data  = json.load(open("data.json"))

x ="y"
while x == "y":
    word = input("Enter word to know its meaning :")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)   
    x = input("do you wamt to countinue: y/n :\n")


    

