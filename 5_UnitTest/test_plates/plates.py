def main():
    is_valid(plate)
    # plate = input("Plates: ").strip()
    # if is_valid(plate):
    #     print("Valid")
    # else:
    #     print("Invalid")


def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum() and plate[0:2].isalpha():
        if len(plate) == 3:
            return True
        elif plate.isalpha():
            return True
        else:
            for i,v in enumerate(plate[2:]):
                if v.isdigit() and v != "0":
                    if plate[i+2:].isdigit():
                        return True
                    else:
                        return False
                else:
                    return False


if __name__ == "__main__":
    main()