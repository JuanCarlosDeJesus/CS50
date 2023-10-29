#  implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
def main():
    time = input("What time is it? ").strip()

    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    prnt = int((int(minutes)/60) * 100)
    return float(f"{int(hours)}.{prnt}")


if __name__ == "__main__":
    main()