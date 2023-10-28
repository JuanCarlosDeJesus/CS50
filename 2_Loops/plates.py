def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        elif s[:2].isalpha():
            if len(s) == 3:
                return True
            elif s[-1].isalpha():
                for _ in s:
                    if _.isnumeric():
                        return False
            elif s[-1].isnumeric():
                for _ in s:
                    if _.isnumeric():
                        if _ == "0":
                            return False
                        else:
                            return True
            # return True
        else:
            return False
    else:
        return False


main()