"""
implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and,
"""
import inflect

p = inflect.engine()

name = []
while True:
    try:
        name.append(input("Name: ").strip())
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(name)}")