import sys

def main():
    n = int(input())
    botas = [[0,0] for i in range(61)]

    for line in sys.stdin:
        if not line:
            break

        m, l = line.strip().split(' ')
        m = int(m)

        pe = 0 if l == 'E' else 1

        botas[m][pe] += 1

    total = 0
    for bota in botas: # O(1)
        total += min(bota[0], bota[1])

    print(total)
    return

main()
