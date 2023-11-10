"""
Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
"""
grocery = {}
while True:
    try:
        itm = input()
        itm = itm.upper()
        if itm not in grocery:
            grocery[itm] = 1
        else:
            grocery[itm] = grocery.get(itm) + 1
    except EOFError:
        break

for k,v in sorted(grocery.items()):
    print(f"{v} {k}")