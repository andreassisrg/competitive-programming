import sys


def main():
    _ = input()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            return
        x, y = line.split(' ')
        second_line = input().strip()
        a, b = second_line.split(' ')
        solve(int(x), int(y), int(a), int(b))


def solve(x, y, a, b):
    total_amount = 0
    if x > 0 and y > 0 and b < (2 * a):
        min_val = min(x, y)
        total_amount += b * min_val
        x -= min_val
        y -= min_val

    if x > 0 or y > 0:
        total_amount += (x + y) * a

    print(total_amount)


main()
