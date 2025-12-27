import sys

def main():
    _ = int(input())
    for line in sys.stdin:
        line = line.strip()
        if not line:
            return
        x, n, m = line.split(' ')
        solve(int(x), int(n), int(m))

def solve(x, n, m):
    while n > 0 and x > 20: 
        x = (x // 2) + 10
        n -= 1
    
    while m > 0:
        x -= 10
        m -= 1

    if x <= 0:
        print('YES')
        return

    print('NO')

main()
