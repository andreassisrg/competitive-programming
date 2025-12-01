import sys

def main():
    i = 1
    for line in sys.stdin:
        n = int(line)
        print("Instancia", i)
        print(solve(n))
        i += 1

# first non-zero digits from 0-9
digits = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def solve(n):
    """
    Let D(n) be the last non-zero digit in n!
    If tens digit (or second last digit) of n is odd
        D(n) = 4 * D(floor(n/5)) * D(Unit digit of n) 
    If tens digit (or second last digit) of n is even
        D(n) = 6 * D(floor(n/5)) * D(Unit digit of n)
    """
    
    if n < 10:
        return digits[n]

    second_last_digit = (n % 100) // 10
    last_digit = n % 10

    if second_last_digit % 2 != 0:
        return (4 * solve(n//5) * digits[last_digit]) % 10
    elif second_last_digit % 2 == 0:
        return (6 * solve(n//5) * digits[last_digit]) % 10 

    return 0

main()
