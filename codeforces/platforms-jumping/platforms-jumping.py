def main():
    n, m, d = input().split(' ')
    n, m, d = int(n), int(m), int(d)
    c = input().split(' ')
    c = [int(i) for i in c]

    jumps = list()
    platformIndex = 1
    remaining = c[platformIndex - 1]
    while platformIndex <= m:
        jumps.extend([0 for _ in range(d - 1)])

        remaining = c[platformIndex - 1]
        while remaining > 0:
            jumps.append(platformIndex)
            remaining -= 1

        platformIndex += 1

    # in case there arent enough platforms or not big enough jumps
    if len(jumps) < n:
        if len(jumps) + d <= n:
            print('NO')
            return
        else:
            jumps.extend([0 for _ in range(d - 1)])

    print('YES')
    length = len(jumps)
    for i in range(length):
        if length > n and jumps[i] == 0:
            length -= 1
            continue
        else:
            print(jumps[i], end=' ')
    print()


main()
