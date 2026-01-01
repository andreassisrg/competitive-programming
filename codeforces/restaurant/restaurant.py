def main():
    n = int(input())
    orders = []
    for _ in range(n):
        l, r = input().split(' ')
        l, r = int(l), int(r)
        orders.append((l, r))

    orders.sort(key=lambda order: order[1])

    rentals = 0
    currentOrder = (-1, -1)
    for order in orders:
        if order[0] > currentOrder[1]:
            currentOrder = order
            rentals += 1

    print(rentals)


main()
