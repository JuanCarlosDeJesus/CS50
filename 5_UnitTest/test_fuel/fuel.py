"""
ReFuel
"""
def main():
    print(gauge(convert(input("Fraction: "))))



def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            else:
                return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage > 1:
        return f"{percentage}%"
    else:
        return "E"



if __name__ == "__main__":
    main()
