# This app omits all the vowels in a sentence. whether upper or lower case.

def omit():
    omt = input("Input: ")
    print("Output: ", end="")
    for _ in omt:
        if _ in ["A","E","I","O","U","a","e","i","o","u"]:
            print("", end="")
        else:
            print(_, end="")
    print()
    
def main():
    omit()

main()