"""
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the users greeting,
and treat the users greeting case-insensitively.
"""

def main():
    value(greeting)


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()