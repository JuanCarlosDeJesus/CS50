# convert camel case var to snake case

def camelCase(cmlCse):
    snake_case = ""
    for _ in cmlCse:
        if _.isupper():
            snake_case += "_" + _.lower()
        else:
            snake_case += _
    return snake_case


def main():
    cmlCse = input("camelCase: ")
    print(f"snake_case: {camelCase(cmlCse)}")

main()