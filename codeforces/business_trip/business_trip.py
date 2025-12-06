def main():
    k = int(input())
    a = list(map(int, input().split())) # O(n) - space
    
    if k == 0:
        print(0)
        return

    a.sort(reverse=True) # O(n logn) - time

   current_size, min_months = 0, 0
    for i in range(len(a)): # O(n) - time
        current_size += a[i]
        min_months += 1
        if current_size >= k:
            print(min_months)
            return

    print(-1)
    return

main()
