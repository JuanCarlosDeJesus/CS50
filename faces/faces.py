# This is an emoji converter program

def convert(message):
    message = message.split()
    for word in message:
        if word == ":)":
            print("\U0001F642", end=" ")
        elif word == ":(":
            print("\U0001F641", end=" ")
        else:
            print(word, end=" ")

    print()


message = input()
convert(message)