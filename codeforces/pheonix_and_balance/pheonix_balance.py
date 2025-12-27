import sys


def main():
    _ = int(input())
    for line in sys.stdin:
        line = line.strip()
        if not line:
            return
        solve(int(line))


def solve(n):
    coins = [2**i for i in range(1, n+1)]

    pile1 = coins.pop()
    pile2 = coins.pop()
    amount_pile1, amount_pile2 = 1, 1
    max = n / 2

    while len(coins) > 0:
        if pile1 >= pile2:
            if amount_pile2 < max:
                pile2 += coins.pop()
                amount_pile2 += 1
            else:
                pile1 += coins.pop()
                amount_pile1 += 1

        else:
            if amount_pile1 < max:
                pile1 += coins.pop()
                amount_pile1 += 1
            else:
                pile2 += coins.pop()
                amount_pile2 += 1

    print(abs(pile1 - pile2))


main()
