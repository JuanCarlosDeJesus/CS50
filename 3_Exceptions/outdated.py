"""
 implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
 wherein the month in the latter might be any of the values in the list "dt". Then output that same date in YYYY-MM-DD format. If the users
 input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether
 a month has 28, 29, 30, or 31 days.
"""
def mon(MM):
    mm = {
        "01":["January","1"],
        "02":["February","2"],
        "03":["March","3"],
        "04":["April","4"],
        "05":["May","5"],
        "06":["June","6"],
        "07":["July","7"],
        "08":["August","8"],
        "09":["September","9"],
        "10":["October","10"],
        "11":["November","11"],
        "12":["December","12"]
    }

    for k,v in mm.items():
        if MM in v:
            return k


def day(DD):
    if "," in DD:
        DD = DD.strip(",")

    if 1 <= int(DD) <= 9:
        return "0" + DD
    elif 10 <= int(DD) <= 31:
        return DD


def get_date():
    while True:
        prompt = input("Date: ").strip()
        if " " in prompt and "," in prompt:
            MM, DD, YY = prompt.split(" ")
            if MM.isalpha():
                if mon(MM) is not None and day(DD) is not None:
                    return f"{YY}-{mon(MM)}-{day(DD)}"
        elif "/" in prompt:
            MM, DD, YY = prompt.split("/")
            if not MM.isalpha():
                if mon(MM) is not None and day(DD) is not None:
                    return f"{YY}-{mon(MM)}-{day(DD)}"


def main():
    dt = get_date()
    print(dt)


if __name__ == "__main__":
    main()