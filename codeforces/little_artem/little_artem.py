import sys
import math

def main():
    t = int(input())
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            return

        n, m = line.split(' ')

        solve(int(n), int(m))

def solve(n, m):
    for i in range(n):
        row = []
        for j in range(m):
            if i == 0 and j == 0:
                row.append('W')
            else:
                row.append('B')
        print(''.join(row))

main()
