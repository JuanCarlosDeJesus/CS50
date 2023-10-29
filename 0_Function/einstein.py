# Python program to calculate the value of energy given the mass

def energy(m):
    e = int(m) * (300000000 ** 2)
    return print(e)

def main():
    m = input("m: ")
    energy(m)

main()