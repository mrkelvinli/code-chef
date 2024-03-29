import sys
from math import floor

# cache in hash
cache = {0:0}

def break_down (coin):
    #  check if the num is already in our cache
    if coin in cache:
        return cache[coin]
    else :
        sol = max(coin, break_down(int(coin/2)) + break_down(int(coin/3)) + break_down(int(coin/4)))
        cache[coin] = sol
        return sol

if __name__ == "__main__":
    while True:
        try:
            num = int(raw_input())
            print break_down(num)
            # sys.stdout.write("%d\n" % break_down(num))
        except:
            break
