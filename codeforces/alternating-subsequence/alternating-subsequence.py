import math


def main():
    t = int(input())
    for _ in range(t):
        solve()


def solve():
    _ = int(input())
    a = input().split(' ')
    a = [int(x) for x in a]

    maxSum = 0
    localMax = a[0]

    for i in range(1, len(a)):
        if changedSign(a[i-1], a[i]):
            maxSum += localMax
            localMax = -math.inf

        if a[i] > localMax:
            localMax = a[i]

    maxSum += localMax

    print(maxSum)


def changedSign(previous, current):
    if current > 0 and previous < 0:
        return True

    if current < 0 and previous > 0:
        return True

    return False


main()
