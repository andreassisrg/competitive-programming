factorials = [1, 1]

def main():
    n = int(input())

    res = []
    i = 1
    while n > 0:
        if factorial(i) > n:
            res.append(factorial(i-1))
            n -= factorial(i-1)
            i = 0

        i += 1

    print(len(res))

def factorial(x):
    try:
        res = factorials[x]
        return res
    except IndexError:
        factorials.append(factorial(x-1) * x)
        return factorials[x]

main()
