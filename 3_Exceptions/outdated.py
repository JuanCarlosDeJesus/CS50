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
    if 1 <= DD >= 31:
        if "," in DD:
            return DD.strip(",")
        else:
            return DD

def get_date():
    while True:
        try:
            prompt = input("Date: ").strip()
            
            if " " in prompt:
                MM, DD, YY = prompt.split(" ")
                if MM.isalpha():
                    print(f"{YY}-{mon(MM)}-{day(DD)}")
                else:
                    continue
                break
            elif "/" in prompt:
                MM, DD, YY = prompt.split("/")
                print(f"{YY}-{mon(MM)}-{day(DD)}")
                break
        except:
            pass

def main():
    if __name__ == "__main__":
        get_date()

main()