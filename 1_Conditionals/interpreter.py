# a program that prompts the user for an arithmetic expression and then calculates and outputs the result
# as a floating-point value formatted to one decimal place.

x, y, z = input("Expresion: ").strip().split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(round(float(x) / float(z),1))