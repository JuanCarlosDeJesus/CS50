"""
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the users greeting,
and treat the users greeting case-insensitively.
"""
greet = input("Greeting: ").strip().lower()
if "hello" in greet:
    print("$0")
elif "h" in greet[0]:
    print("$20")
else:
    print("$100")