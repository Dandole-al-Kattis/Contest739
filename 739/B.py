

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        a, b, c = list(map(int, input().split()))
        n = abs(b - a) * 2
        if c > n:
            print(-1)
        elif abs(a - b) < n//2:
            print(-1)
        else:
            print(c + n//2)
