import requests
import json

# Step 1 empty dict to start & then starter currency
currency_cache = {}
currency_code = input().lower()

# Step 2 request data & start that cache
currency_rate = requests.get(f'http://www.floatrates.com/daily/{currency_code}.json')

# apparently they may start with USD or EUR so lets MAKE SURE THEY DON'T
# AND IF THEY DO THEN SKIP CACHING THEM BECAUSE IT JUST THROWS ERRORS.
if currency_code != 'usd':
    currency_cache['usd'] = currency_rate.json()['usd']

if currency_code != 'eur':
    currency_cache['eur'] = currency_rate.json()['eur']

while True:
    # Step 3 take the other currency code and number
    exchange_code = input().lower()

    # Step 'end-this' -- if the input is empty break the while loop
    if exchange_code == '':
        break

    # Make sure to do this AFTER CHECKING IF THE INPUT IS EMPTY otherwise
    # you fail.
    total = float(input())
    print("Checking the cache...")
    # Step 4 if currency is in the cache
    if exchange_code in currency_cache:
        print("Oh! It is in the cache!")

        retrieve_rate = currency_cache[exchange_code]['rate']
        print(f'You received {round(total * retrieve_rate, 2)} {exchange_code.upper()}.')
    # Step 5 if currency is not in the cache & adding it to the cache
    elif exchange_code not in currency_cache:
        print("Sorry, but it is not in the cache!")

        currency_cache[exchange_code] = currency_rate.json()[exchange_code]
        retrieve_rate = currency_cache[exchange_code]['rate']
        print(f'You received {round(total * retrieve_rate, 2)} {exchange_code.upper()}.')
