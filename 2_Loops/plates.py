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

# def main():
#     plate = input("Plates: ").strip()
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(plate):
#     if 2 <= len(plate) <= 6 and plate.isalnum() and plate[0:2].isalpha():
#         if len(plate) == 3:
#             return True
#         elif plate.isalpha():
#             return True
#         else: 
#             for i,v in enumerate(plate[2:]):
#                 if v.isdigit() and v != "0":
#                     if plate[i+2:].isdigit():
#                         return True
#                     else:
#                         return False
#                 else:
#                     return False


# if __name__ == "__main__":
#     main()s