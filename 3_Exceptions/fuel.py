"""
implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate
that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
"""
def main():
    x = get_fuel("Fraction: ")
    print(x)


def convert(x,y):
    fuel = ((x/y)*100)
    fuel = round(fuel)
    if fuel >= 99:
        return "F"
    elif fuel > 1:
        return f"{int(fuel)}%"
    else:
        return "E"


def get_fuel(prompt):
    while True:
        try:
            x, y = input(prompt).strip().split("/")
            if (x.isdigit() and y.isdigit()) and (int(x) <= int(y)) and (int(y) > 0):
                return convert(int(x),int(y))
        except (ValueError, ZeroDivisionError):
            pass


main()