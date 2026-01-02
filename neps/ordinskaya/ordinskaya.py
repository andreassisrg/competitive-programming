import math


def main():
    n, m = input().split(' ')
    n, m = int(n), int(m)
    dives = input().split(' ')
    dives = [int(dive) for dive in dives]

    # normalize everything to get the min
    # make everything in the list to be lower half of m
    normalizationLimit = math.ceil(m/2)
    for i in range(len(dives)):
        if dives[i] >= normalizationLimit:
            dives[i] = m - dives[i]

    totalDepth = dives[0]
    for i in range(1, len(dives)):
        if dives[i] >= dives[i-1]:
            totalDepth += dives[i]
            continue

        shift = m - dives[i]

        if shift < dives[i - 1]:
            print(-1)
            return

        totalDepth += shift
        dives[i] = shift

    print(totalDepth)


main()
