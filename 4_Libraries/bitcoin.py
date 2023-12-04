"""
implement a program that:
Expects the user to specify as a command-line argument the number of Bitcoins, n that they would like to buy.
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
"""
import sys
import requests
import json

if len(sys.argv) > 1:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(json.dumps(response.json(), indent=2))
    bit = response.json()
    rate = bit["bpi"]["USD"]["rate_float"]
    print(f"${n * rate:,.4f}")

except requests.RequestException:
    pass