def main():
    n, m = input().split(' ')
    n, m = int(n), int(m)
    pins = input().split(' ')
    pins = [int(pin) for pin in pins]

    totalMovements = 0
    for i in range(0, len(pins) - 1):
        heightShift = m - pins[i]

        pins[i] += heightShift
        pins[i+1] += heightShift

        totalMovements += abs(heightShift)

    print(totalMovements)


main()
