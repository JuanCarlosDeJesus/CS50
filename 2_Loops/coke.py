# this is a coke vendor machine app. at 50 a bottle, users will enter coins ranging from 25,10, to 5 in value.
# you will setup a int var that will have a value 0. as buyers deposit coins to the machine a running total will be calculated.
# when it reaches 50 or more, the app will stop accepting deposits and will give change if necessary.

def running_total():
    coin_total = 0
    amount_due = 50
    insert_coin = 0
    while coin_total < 50:
        print(f"Amount Due: {50 - coin_total}")
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in [5,10,25]:
            coin_total += insert_coin
        else:
            continue

    print(f"Change Owed: {coin_total - amount_due}")

def main():
    running_total()

if __name__ == "__main__":
    main()