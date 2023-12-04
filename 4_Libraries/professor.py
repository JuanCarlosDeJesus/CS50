"""
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
and generate_integer returns a randomly generated non-negative integer with n level digits or raises a ValueError if level is not 1, 2, or 3:
"""
import random


def main():
    score = 0
    level = get_level()
    t = 1
    while t <= 10:
        x,y = generate_integer(level)
        attempt = 1
        while attempt <= 3:
            try:
                if x + y != int(input(f"{x} + {y} = ")):
                    if attempt == 3:
                        print(f"{x} + {y} = {x+y}")
                        break
                    else:
                        attempt += 1
                        print("EEE")
                else:
                    score += 1
                    attempt = 3
                    break
            except ValueError:
                attempt += 1
                print("EEE")
        t += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1,2,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return [x, y]
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return [x, y]
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return [x, y]


if __name__ == "__main__":
    main()
