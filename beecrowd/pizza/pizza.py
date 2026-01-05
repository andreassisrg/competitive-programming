def main():
    n = int(input())
    k = input().split(' ')
    k = [int(i) for i in k]

    k += k
    globalMax = 0
    localMax, localMaxLength = 0, 0
    buffer, bufferLength = 0, 0
    for num in k:


main()
