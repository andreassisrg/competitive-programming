def main():
    _ = input()
    portas = input().split(' ')
    portas = [int(porta) for porta in portas]

    maxGlobal, maxLocal, localSub = 0, 0, 0
    for porta in portas:
        if porta <= 0:
            if localSub > maxLocal:
                maxLocal = localSub
            localSub = 0

        maxLocal += porta
        if porta > 0:
            localSub += porta

        if maxLocal > maxGlobal:
            maxGlobal = maxLocal

    print(maxGlobal)


main()
