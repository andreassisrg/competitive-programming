import sys

def main():
    t = int(input())
    for line in sys.stdin:
        line = line.strip()
        if not line:
            return

        word, bracelet = line.split(' ')

        solve(word, bracelet)

    return

def solve(word, bracelet):
    bracelet *= 2
    reversed_bracelet = bracelet[::-1]

    if bracelet.find(word) != -1 or reversed_bracelet.find(word) != -1: # O(n * m)
        print('S')
        return

    print('N')
    return

main()
