from collections import deque


def main():
    _ = int(input())
    a = input().split(' ')
    a = [int(x) for x in a]

    leftHeights = deque([min(a[0], 1)])
    rightHeights = deque([min(a[-1], 1)])

    for i in range(1, len(a)):
        colHeight = a[i]
        localTriangleHeight = min(leftHeights[i-1] + 1, colHeight)
        leftHeights.append(localTriangleHeight)

    for j in range(len(a) - 2, -1, -1):
        colHeight = a[j]
        localRightTriangle = min(rightHeights[0] + 1, colHeight)
        rightHeights.appendleft(localRightTriangle)

    finalHeights = [min(leftHeights[i], rightHeights[i])
                    for i in range(len(a))]

    print(max(finalHeights))


main()
