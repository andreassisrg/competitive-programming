import sys

def main():
    p = int(input())
    
    for word in sys.stdin:
        word = word.strip()
        if not word:
            return

        solve(word)

    return

def solve(word):
    lowered_word = word.lower()

    for i in range(0, len(lowered_word) - 1):
        if lowered_word[i] >= lowered_word[i + 1]:
            print(f'{word}: N')
            return

    print(f'{word}: O')
    return

main()
