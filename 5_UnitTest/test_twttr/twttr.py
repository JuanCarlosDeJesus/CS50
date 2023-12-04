# This app omits all the vowels in a sentence. whether upper or lower case.

def main():
    shorten(word)


def shorten(word):
    shrtn = ""
    for _ in word:
        if _ not in ["A","E","I","O","U","a","e","i","o","u"]:
            shrtn += _

    return shrtn


if __name__ == "__main__":
    main()
